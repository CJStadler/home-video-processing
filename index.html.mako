<%!
  import datetime
%>

<html>
  <head>
    <title>Stadler-Velie Home Videos</title>
  </head>
  <body>
    <h1>Stadler-Velie Home Videos</h1>
    <p>TODO: description</p>

    <h2>Videos</h2>
    <ol id="table-of-contents">
      % for i, video in enumerate(videos):
        <li><a href="#video_${i}">${video.display_name()}</a></li>
      % endfor
    </ol>

    <div id="videos">
      % for i, video in enumerate(videos):
        <div id="video_${i}">
          <h3>${video.display_name()}</h3>
          <a href="${video.filename}">${video.filename}</a>
          <h4>Scenes</h4>
          <ol class="scenes">
            % for j, scene in enumerate(video.scenes):
              <li class="scene" id="video_${i}_scene${j}">
                <a href="${video.filename}#t=${scene.start_second}">
                  <img src=${thumbnails_directory / video.name() / "{}.jpeg".format(scene.thumbnail_second)}>
                </a>
                <ul>
                  <li>
                    Starts at
                    <a href="${video.filename}#t=${scene.start_second}">${datetime.timedelta(seconds=scene.start_second)}</a>
                  </li>
                  <li>Duration: ${datetime.timedelta(seconds=(scene.end_second - scene.start_second))}</li>
                  <li>Date: ${scene.date}</li>
                  <li>Location: ${scene.location}</li>
                  <li>People: ${", ".join(scene.people)}</li>
                  <li>Description: ${scene.description}</li>
                </ul>
              </li>
            % endfor
          </ol>
        </div>
      % endfor
    </div>
  </body>
</html>
