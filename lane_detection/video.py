import cv2
import numpy as np

vidcap = cv2.VideoCapture('vid/challenge.mp4')
success,image = vidcap.read()
height, width, layers = image.shape


# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
# ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
# args = vars(ap.parse_args())
#
# # Arguments
# dir_path = '.'
# ext = args['extension']
# output = args['output']


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('vid/layers/video.mp4', fourcc, 20, (width, height))


count = 0
while success:

  # cv2.imwrite("img/vid-after/original-frames/frame%d.jpg" % count, image)     # save frame as JPEG file




  gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  # cv2.imwrite("img/vid-after/grayscale/frame%d.jpg" % count, gray)  # save frame as JPEG file



  # Define a kernel size, apply Gaussian smoothing
  kernel_size = 5
  blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
  # cv2.imwrite("img/vid-after/blurred_grayscale/frame%d.jpg" % count, blur_gray)  # save frame as JPEG file



  # Define parameters for Canny and apply. The ration should be 1:2 or 1:3
  low_threshold = 100
  high_threshold = 200
  edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
  # cv2.imwrite("img/vid-after/canny-edge-frames/frame%d.jpg" % count, edges)  # save frame as JPEG file



  # Next we'll create a masked edges image using cv2.fillPoly()
  mask = np.zeros_like(edges)
  ignore_mask_color = 255




  # This time we are defining a four sided polygon to mask
  imshape = image.shape
  vertices = np.array([[(273, 657), (600, 448), (734, 446), (1093, 662)]], dtype=np.int32)  # (imshape[0], imshape[1]) = (540, 960)
  cv2.fillPoly(mask, vertices, ignore_mask_color)
  masked_edges = cv2.bitwise_and(edges, mask)




  # Define the Hough transform parameters
  # Make a blank the same size as our image to draw on
  rho = 1  # distance resolution in pixels of the Hough grid
  theta = np.pi / 180 * 5  # angular resolution in radians of the Hough grid
  threshold = 10  # minimum number of votes (intersections in Hough grid cell)
  min_line_length = 70  # minimum number of pixels making up a line
  max_line_gap = 100  # maximum gap in pixels between connectable line segments
  line_image = np.copy(image) * 0  # creating a blank to draw lines on

  # Run Hough on edge detected image
  # Output "lines" is an array containing endpoints of detected line segments
  lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                          min_line_length, max_line_gap)

  # Iterate over the output "lines" and draw lines on a blank image
  if lines is not None:
    for line in lines:
      for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)




  # Create a "color" binary image to combine with line image
  color_edges = np.dstack((edges, edges, edges))

  # Draw the lines on the edge image
  lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
  cv2.imwrite("img/vid-after/lanes_detected/frame%d.jpg" % count, lines_edges)  # save frame as JPEG file



  # CREATE A VIDEO
  # video.write(lines_edges)


  # cv2.imwrite("img/vid-after/canny-edge-frames/frame%d.jpg" % count, lines_edges)  # save frame as JPEG file


  success,image = vidcap.read()
  print('Read a new frame: ', success, count)
  count += 1


# cv2.destroyAllWindows()
# video.release()