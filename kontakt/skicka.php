<?php
/*
 * Sends the two forms on /kontakt/ to the practice by email.
 *
 * Hand-written, not generated: tools/build-site.py only points the forms here
 * (and only when PREVIEW is off). Works on PHP 7.4 and later. Mail goes out
 * through the host's own mail(), so it passes the domain's SPF record.
 */

// Where messages go. Change this if the practice wants them somewhere else.
const MAIL_TO = 'kontakt@kbt-konsulterna.se';
// The sender. Must be an address on this domain, or SPF fails and the mail
// lands in spam. The visitor's own address goes in Reply-To instead.
const MAIL_FROM = 'kontakt@kbt-konsulterna.se';

const FORMS = [
    'privat' => [
        'title'   => 'Frågor eller förfrågan om tid',
        'subject' => 'Förfrågan via hemsidan',
        'who'     => 'namn',
        // field => [label, required]
        'fields'  => [
            'namn'       => ['Namn', true],
            'epost'      => ['E-post', true],
            'telefon'    => ['Telefon', false],
            'hittade'    => ['Hur hittade du oss', false],
            'meddelande' => ['Meddelande', true],
        ],
    ],
    'foretag' => [
        'title'   => 'Förfrågan om uppdrag (företag/organisation)',
        'subject' => 'Uppdragsförfrågan via hemsidan',
        'who'     => 'foretag',
        'fields'  => [
            'foretag'       => ['Företag / organisation', true],
            'kontaktperson' => ['Kontaktperson', true],
            'epost'         => ['E-post', true],
            'telefon'       => ['Telefon', true],
            'hittade'       => ['Hur hittade du oss', false],
            'meddelande'    => ['Meddelande', false],
        ],
    ],
];

date_default_timezone_set('Europe/Stockholm');

function go($page)
{
    header('Location: /kontakt/' . $page, true, 303);
    exit;
}

// Trimmed text with control characters removed. Only the message may keep
// line breaks; every other value ends up on one line.
function field($name, $multiline)
{
    $v = isset($_POST[$name]) && is_string($_POST[$name]) ? $_POST[$name] : '';
    $v = str_replace("\r\n", "\n", $v);
    $v = preg_replace($multiline ? '/[^\P{C}\n\t]/u' : '/\p{C}/u', ' ', $v);
    if ($v === null) {                     // not valid UTF-8
        return '';
    }
    return trim(mb_substr($v, 0, $multiline ? 5000 : 200));
}

// Encoded header text, folded so long subjects stay within the mail line limit.
function mime($text)
{
    return mb_encode_mimeheader($text, 'UTF-8', 'B', "\r\n");
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    go('');
}

// Spam trap: people never see this field, bots fill it. Look like a success
// so they get no signal to adapt to.
if (field('webbplats', false) !== '') {
    go('tack.html');
}

$kind = field('formular', false);
if (!isset(FORMS[$kind])) {
    go('fel.html');
}
$form = FORMS[$kind];

$values = [];
foreach ($form['fields'] as $name => [$label, $required]) {
    $values[$name] = field($name, $name === 'meddelande');
    if ($required && $values[$name] === '') {
        go('fel.html');
    }
}
$email = filter_var($values['epost'], FILTER_VALIDATE_EMAIL);
if ($email === false) {
    go('fel.html');
}

$lines = [$form['title'], ''];
foreach ($form['fields'] as $name => [$label, $required]) {
    if ($name !== 'meddelande') {
        $lines[] = $label . ': ' . ($values[$name] !== '' ? $values[$name] : '–');
    }
}
$lines[] = '';
$lines[] = 'Meddelande:';
$lines[] = $values['meddelande'] !== '' ? $values['meddelande'] : '–';
$lines[] = '';
$lines[] = '-- ';
$lines[] = 'Skickat från kontaktformuläret på kbt-konsulterna.se, ' . date('Y-m-d H:i') . '.';
$lines[] = 'Svara på det här mejlet så går svaret direkt till avsändaren.';
$body = implode("\r\n", str_replace("\n", "\r\n", $lines));

$subject = $form['subject'] . ' – ' . $values[$form['who']];
$headers = implode("\r\n", [
    'From: ' . mime('KBT-Konsulterna hemsida') . ' <' . MAIL_FROM . '>',
    'Reply-To: ' . $email,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
]);

$sent = mail(MAIL_TO, mime($subject), $body, $headers, '-f' . MAIL_FROM);
go($sent ? 'tack.html' : 'fel.html');
