import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>My Favourite Movie Trailers!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
		.navbar {background:#3f5d71;}
		.navbar a.navbar-brand{color:#fff}
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
		.movie-tile .movie_image{position:relative;overflow:hidden;width:220px;margin:0 auto;}
		.movie-tile .movie_image img{position:relative;overflow:hidden}
		.movie-tile .movie_image .movie_trailer_button{position:absolute;display:none;vertical-align: middle;-webkit-transform: translateZ(0);transform: translateZ(0);box-shadow: 0 0 1px rgba(0, 0, 0, 0);-webkit-backface-visibility: hidden;backface-visibility: hidden;-moz-osx-font-smoothing: grayscale;-webkit-transition-property: color;transition-property: color;-webkit-transition-duration: 0.5s;transition-duration: 0.5s;}
		.movie-tile .movie_image .movie_trailer_button:before{content: "";position: absolute;z-index: -1;top: 0;left: 0;right: 0;bottom: 0;background: #3f5d71;-webkit-transform: scaleX(0);transform: scaleX(0);-webkit-transform-origin: 0 50%;transform-origin: 0 50%;-webkit-transition-property: transform;transition-property: transform;-webkit-transition-duration: 0.5s;transition-duration: 0.5s;-webkit-transition-timing-function: ease-out;transition-timing-function: ease-out;}
		.movie-tile .movie_image .movie_trailer_button:hover:before, .movie-tile .movie_image .movie_trailer_button:focus:before, .movie-tile .movie_image .movie_trailer_button:active:before {-webkit-transform: scaleX(1);transform: scaleX(1);-webkit-transition-timing-function: cubic-bezier(0.52, 1.64, 0.37, 0.66);transition-timing-function: cubic-bezier(0.52, 1.64, 0.37, 0.66);}
		.movie-tile .movie_image:hover .movie_trailer_button{display:block;width:220px;height:342px;left:0;right:0;top:0;margin:0 auto;opacity:0.85}
		.movie-tile .movie_image .movie_trailer_button h3{cursor:pointer;color:#fff;display:inline-block;background:#000;text-shadow:none;padding:5px 10px;transition: all .2s ease-in-out;font-size:18px}
		.movie-tile .movie_image .movie_trailer_button h3:hover{transform: scale(1.1);}
		.movie-tile .movie_image .movie_trailer_button h4{color:#fff;margin-top:100px;margin-bottom:5px;font-size:19px}
		.movie-tile .movie_image .movie_trailer_button p{color:#fff;margin-bottom:5px;}
		.movie-tile .movie_image .movie_trailer_button span{color:#fff}
		.movie-tile h2{font-size:25px}
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">My Favourite Movie Trailers!</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
	<div class="movie_image">
		<img src="{poster_image_url}" width="220" height="342">
		<div class="movie_trailer_button">
			<h4>{movie_title}</h4>
			<p>Released On:{release_date}</p>
			<span>Earned:{earnings}</span>
			<h3>Watch Trailer Now!</h3>
		</div>
	</div>
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
			release_date=movie.release_date,
			earnings=movie.earnings,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible