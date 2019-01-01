<html>
  <head>
    <title>Stadler-Velie Home Videos</title>
  </head>
  <body>
    <h1>Stadler-Velie Home Videos</h1>
    <p>TODO: description</p>

    <ol id="table-of-contents">
      % for i, video in enumerate(videos):
        <li><a href="#video_${i}">${video.title()}</a></li>
      % endfor
    </ol>
  </body>
</html>
