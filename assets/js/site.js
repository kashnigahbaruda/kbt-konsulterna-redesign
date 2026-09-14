/* KBT-Konsulterna — progressive enhancement only.
   Every page works with this file absent. */
(function () {
  'use strict';

  /* Mobile navigation */
  var burger = document.querySelector('.burger');
  var mnav = document.querySelector('.mobile-nav');
  if (burger && mnav) {
    /* The panel is fixed below the header, so it needs the header's real
       height. Measured rather than hard-coded in case the header wraps. */
    var syncHeadHeight = function () {
      var h = document.querySelector('.site-head__inner');
      if (h) {
        document.documentElement.style.setProperty(
          '--head-h', Math.round(h.getBoundingClientRect().height) + 'px');
      }
    };
    syncHeadHeight();
    window.addEventListener('resize', syncHeadHeight);

    var setOpen = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      mnav.setAttribute('data-open', String(open));
      if (open) {
        syncHeadHeight();
        mnav.scrollTop = 0;
      }
    };

    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });

    /* Close on Escape, and return focus to the toggle */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        burger.focus();
      }
    });

    /* Never leave the lock on if the menu stops being reachable, e.g. the
       viewport widens past the desktop breakpoint while it is open. */
    var mq = window.matchMedia('(min-width: 66rem)');
    var onChange = function () { if (mq.matches) setOpen(false); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }

  /* Header gets a hairline shadow once the page is scrolled, so it separates
     from content without a permanent border. A class rather than an inline
     style, so the look lives in site.css; only touched when the state flips. */
  var head = document.querySelector('.site-head');
  if (head) {
    var scrolled = null;
    var onScroll = function () {
      var now = window.scrollY > 12;
      if (now !== scrolled) {
        scrolled = now;
        head.classList.toggle('is-scrolled', now);
      }
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Reveal-on-scroll for section heads (heading and text together), cards,
     steps and router rows. Elements start hidden only when this runs, so a
     no-JS visitor sees everything. */
  var targets = document.querySelectorAll('[data-reveal]');
  if (targets.length) {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || !('IntersectionObserver' in window)) {
      targets.forEach(function (el) { el.setAttribute('data-seen', 'true'); });
      return;
    }
    /* Whatever comes into view together (a row of portraits, the four steps)
       arrives in document order a beat apart. Anything scrolled to later
       appears without waiting on its neighbours. The delay is cleared once the
       reveal has run so it cannot linger on later transitions. */
    var io = new IntersectionObserver(function (entries) {
      var hits = [];
      entries.forEach(function (entry) {
        if (entry.isIntersecting) hits.push(entry.target);
      });
      hits.sort(function (a, b) {
        return a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1;
      });
      hits.forEach(function (el, i) {
        if (i) {
          el.style.transitionDelay = (Math.min(i, 6) * 70) + 'ms';
          var clear = function () {
            el.style.transitionDelay = '';
            el.removeEventListener('transitionend', clear);
          };
          el.addEventListener('transitionend', clear);
        }
        el.setAttribute('data-seen', 'true');
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    /* This script is deferred, so the page has already been painted by the
       time it runs. Anything on screen now must be left alone: hiding it would
       make it blink out and fade back in. Only what is still below the fold
       (or above, on a restored scroll position) is hidden and revealed.
       Every rect is read before any class is written, so the loop causes one
       layout rather than one per element. */
    var vh = window.innerHeight || document.documentElement.clientHeight;
    var onScreen = Array.prototype.map.call(targets, function (el) {
      var r = el.getBoundingClientRect();
      return r.top < vh && r.bottom > 0;
    });
    targets.forEach(function (el, i) {
      if (onScreen[i]) {
        el.setAttribute('data-seen', 'true');
      } else {
        el.classList.add('reveal');
        io.observe(el);
      }
    });
  }
})();
