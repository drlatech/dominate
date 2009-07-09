from html import html_tag, ugly, single

COMMON_MAIN   = ['accesskey', 'class', 'contenteditable', 'contextmenu', 'dir', 'draggable', 'id', 'item', 'hidden', 'lang', 'itemprop', 'spellcheck', 'style', 'subject', 'tabindex', 'title']
COMMON_EVENTS = ['onabord', 'onblur', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'oncontextmenu', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleavea', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformchange', 'onforminput', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreadystatechange', 'onscroll', 'onseeked', 'onseeking', 'onselect', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'onvolumechange', 'onwaiting']
COMMON = COMMON_MAIN + COMMON_EVENTS

#Root element
class html(html_tag):
    attributes = COMMON + ['manifest']

#Document metadata
class head(html_tag): valid = COMMON
class title(html_tag): valid = COMMON
class base(html_tag):
    ''' Must contain href, target, or both '''
    valid = COMMON + ['href', 'target']
class link(single):
    valid     = COMMON + ['href', 'rel', 'media', 'hreflang', 'type', 'sizes']
    required  = ['href', 'rel']
class meta(single):
    ''' Must contain one of: name, http-equiv, content, or charset '''
    valid = COMMON + ['name', 'http-equiv', 'content', 'charset']
class style(ugly):
    valid = COMMON + ['media', 'type', 'scoped']

#Scripting
class script(ugly):
    valid = COMMON + ['src', 'async', 'defer', 'type', 'charset']
class noscript(html_tag): valid = COMMON

#Sections
class body(html_tag):
    valid = COMMON + ['onafterprint', 'onbeforeprint', 'onbeforeunload', 'onhashchange', 'onmessage', 'ononline', 'onoffline', 'onpopstate', 'onredo', 'onresize', 'onstorage', 'onundo', 'onunload']
class section(html_tag):
    valid = COMMON + ['cite']
class nav(html_tag): valid = COMMON
class article(html_tag):
    valid = COMMON + ['cite', 'pubdate']
class aside(html_tag): valid = COMMON
class h1(html_tag): valid = COMMON
class h2(html_tag): valid = COMMON
class h3(html_tag): valid = COMMON
class h4(html_tag): valid = COMMON
class h5(html_tag): valid = COMMON
class h6(html_tag): valid = COMMON
class hgroup(html_tag): valid = COMMON
class header(html_tag): valid = COMMON
class footer(html_tag): valid = COMMON
class address(html_tag): valid = COMMON

#Grouping content
class p(html_tag): valid = COMMON
class hr(single): valid = COMMON
class br(single): valid = COMMON
class pre(ugly): valid = COMMON
class dialog(html_tag): valid = COMMON
class blockquote(html_tag):
    valid = COMMON + ['cite']
class ol(html_tag):
    valid = COMMON + ['reversed', 'start']
class ul(html_tag): valid = COMMON
class li(html_tag): valid = COMMON
class dl(html_tag): valid = COMMON
class dt(html_tag): valid = COMMON
class dd(html_tag): valid = COMMON

#Text-level semantics
class a(html_tag):
    valid = COMMON + ['href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type']
class q(html_tag):
    valid = COMMON + ['cite']
class cite(html_tag): valid = COMMON
class em(html_tag): valid = COMMON
class strong(html_tag): valid = COMMON
class small(html_tag): valid = COMMON
class mark(html_tag): valid = COMMON
class dfn(html_tag): valid = COMMON
class abbr(html_tag): valid = COMMON
class time(html_tag):
    valid = COMMON + ['datetime']
class progress(html_tag):
    valid = COMMON + ['value', 'max']
class meter(html_tag):
    valid = COMMON + ['value', 'min', 'low', 'high', 'max', 'optimum']
class code(html_tag): valid = COMMON
class var(html_tag): valid = COMMON
class samp(html_tag): valid = COMMON
class kbd(html_tag): valid = COMMON
class sub(html_tag): valid = COMMON
class sup(html_tag): valid = COMMON
class span(html_tag): valid = COMMON
class i(html_tag): valid = COMMON
class b(html_tag): valid = COMMON
class bdo(html_tag): valid = COMMON
class ruby(html_tag): valid = COMMON
class rt(html_tag): valid = COMMON
class rp(html_tag): valid = COMMON

#Edits
class ins(html_tag):
    valid = COMMON + ['cite', 'datetime']
class _del(html_tag):
    valid = COMMON + ['cite', 'datetime']

#Embedded content
class figure(html_tag): valid = COMMON
class img(html_tag):
    valid    = COMMON + ['alt', 'src', 'usemap', 'ismap', 'width', 'height']
    required = ['src']
class iframe(html_tag):
    valid = COMMON + ['src', 'name', 'sandbox', 'seamless', 'width', 'height']
class embed(html_tag):
    valid = COMMON + ['src', 'type', 'width', 'height']
class object(html_tag):
    valid = COMMON + ['data', 'type', 'name', 'usemap', 'form', 'width', 'height']
class param(html_tag):
    valid = COMMON + ['name', 'value']
class video(html_tag):
    valid = COMMON + ['src', 'poster', 'autobuffer', 'autoplay', 'loop', 'controls', 'width', 'height']
class audio(html_tag):
    valid = COMMON + ['src', 'autobuffer', 'autoplay', 'loop', 'controls']
class source(html_tag):
    valid = COMMON + ['src', 'type', 'media']
class canvas(html_tag):
    valid = COMMON + ['width', 'height']
class map(html_tag):
    valid = COMMON + ['name']
class area(single):
    valid = COMMON + ['alt', 'coords', 'shape', 'href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type']

#Tabular data
class table(html_tag): valid = COMMON
class caption(html_tag): valid = COMMON
class colgroup(html_tag):
    valid = COMMON + ['span']
class tbody(html_tag): valid = COMMON
class thead(html_tag): valid = COMMON
class tfoot(html_tag): valid = COMMON
class tr(html_tag): valid = COMMON
class td(html_tag):
    valid = COMMON + ['colspan', 'rowspan', 'headers']
class th(html_tag):
    valid = COMMON + ['colspan', 'rowspan', 'headers', 'scope']

#Forms
class form(html_tag):
    valid = COMMON + ['accept-charset', 'action', 'autocomplete', 'enctype', 'method', 'name', 'novalidate', 'target']
class fieldset(html_tag):
    valid = COMMON + ['disabled', 'form', 'name']
class label(html_tag):
    valid = COMMON + ['form', 'for']
class input(single):
    valid = COMMON + ['accept', 'alt', 'autocomplete', 'autofocus', 'checked', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'list', 'max', 'maxlength', 'min', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size', 'src', 'step', 'type', 'value', 'width']
class button(html_tag):
    valid = COMMON + ['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'name', 'type', 'value']
class select(html_tag):
    valid = COMMON + ['autofocus', 'disabled', 'form', 'multiple', 'name', 'size']
class datalist(html_tag): valid = COMMON
class optgroup(html_tag):
    valid = COMMON + ['disabled', 'label']
class option(html_tag):
    valid = COMMON + ['disabled', 'label', 'selected', 'value']
class textarea(html_tag):
    valid = COMMON + ['autofocus', 'cols', 'disabled', 'form', 'maxlength', 'name', 'placeholder', 'readonly', 'required', 'rows', 'wrap']
class keygen(html_tag):
    valid = COMMON + ['autofocus', 'challenge', 'disabled', 'form', 'keytype', 'name']
class output(html_tag):
    valid = COMMON + ['for', 'form', 'name']

#Interactive elements
class details(html_tag):
    valid = COMMON + ['open']
class datagrid(html_tag):
    valid = COMMON + ['disabled']
class command(html_tag):
    valid = COMMON + ['type', 'label', 'icon', 'disabled', 'checked', 'radiogroup']
class bb(html_tag):
    valid = COMMON + ['type']
class menu(html_tag):
    valid = COMMON + ['type', 'label']

#Miscellaneous elements
class legend(html_tag): valid = COMMON
class div(html_tag): valid = COMMON