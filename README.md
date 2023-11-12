# Very simple static website generator

This is a very very very minimal and simple python script to create a static website.

If you want a serious and good static site generator use [Hugo](https://github.com/gohugoio/hugo "Hugo").

This tool just replicates the file structure in a folder to another folder but replaces shortcodes with blocks.

Better said (and considering it to be used in websites) it's meant to take html files in a certain folder, recreate the structure in another folder but replacing shortcodes in the format `{{ block block_name }}` with blocks (header, footer, sidebar, ...) found located in another folder.

It also support variables to be declared in the page and used in the blocks.

Example:

`pages/page-1.html`

```
{{ var page_title = About }}
{{ var body_class = page-about }}
{{ block header }}

    <div class="main-block">
      <h1>Hello there!</h1>
    </div>

{{ block footer }}
```

`blocks/header.html`
```
<html>
  <head>
    <title>
      {{ page_title }} - mugnozzo.xyz
    </title>
  </head>
  <body class="{{ body_class }}">
    <header>
      <p>This is my header</p>
    <header>
```

`blocks/footer.html`
```
    <footer>
      <p>This is my footer</p>
    </footer>
  </body>
</html>
```

This will render a single page, starting from `pages/page-1.html` replacing:
- the shortcode `{{ block header }}` with the content of the file `blocks/header.html`
- - the shortcode `{{ block footer }}` with the content of the file `blocks/footer.html`

The variables declared in the first rows of page-1.html are substituted in the blocks with their values.

The result:

```
<html>
  <head>
    <title>
      About - mugnozzo.xyz
    </title>
  </head>
  <body class="page-about">
    <header>
      <p>This is my header</p>
    <header>

    <div class="main-block">
      <h1>Hello there!</h1>
    </div>
    
    <footer>
      <p>This is my footer</p>
    </footer>
  </body>
</html>
```
