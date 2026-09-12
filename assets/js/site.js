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
     from content without a permanent border. */
  var head = document.querySelector('.site-head');
  if (head) {
    var onScroll = function () {
      head.style.boxShadow = window.scrollY > 12
        ? '0 1px 0 0 rgba(27,58,56,0.12)'
        : 'none';
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Reveal-on-scroll for section headings. Elements start hidden only when
     this runs, so a no-JS visitor sees everything. */
  var targets = document.querySelectorAll('[data-reveal]');
  if (targets.length) {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || !('IntersectionObserver' in window)) {
      targets.forEach(function (el) { el.setAttribute('data-seen', 'true'); });
      return;
    }
    targets.forEach(function (el) { el.classList.add('reveal'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.setAttribute('data-seen', 'true');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    targets.forEach(function (el) { io.observe(el); });
  }
})();
