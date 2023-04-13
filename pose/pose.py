def calc_bounding_rect(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_array = np.empty((0, 2), int)

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_point = [np.array((landmark_x, landmark_y))]
        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv2.boundingRect(landmark_array)

    return [x, y, x + w, y + h]

def draw_landmarks(image, landmarks, visibility_th=0.5):
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_point = []

    for index, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_z = landmark.z
        landmark_point.append([landmark.visibility, (landmark_x, landmark_y)])

        if landmark.visibility < visibility_th:
            continue

        point_color = (0, 255, 255)
        if index == 0:  # nose
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 1:  # left_eye_inner
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 2:  # left_eye
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 3:  # left_eye_outer
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 4:  # right_eye_inner
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 5:  # right_eye
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 6:  # right_eye_outer
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 7:  # left_ear
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 8:  # right_ear
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 9:  # mouth_left
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 10:  # mouth_right
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 11:  # left_shoulder
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 12:  # right_shoulder
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 13:  # left_elbow
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 14:  # right_elbow
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 15:  # left_wrist
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 16:  # right_wrist
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 17:  # left_pinky
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 18:  # right_pinky
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 19:  # left_index
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 20:  # right_index
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 21:  # left_thumb
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 22:  # right_thumb
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 23:  # left_hip
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 24:  # right_hip
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 25:  # left_knee
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 26:  # right_knee
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 27:  # left_ankle
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 28:  # right_ankle
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 29:  # left_heel
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 30:  # right_heel
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 31:  # left_foot_index
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)
        if index == 32:  # right_foot_index
            cv2.circle(image, (landmark_x, landmark_y), 5, point_color, 2)

        if plot_landmark_z:
            cv2.putText(image, "z:" + str(round(landmark_z, 3)),
                       (landmark_x - 10, landmark_y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, point_color, 1,
                       cv2.LINE_AA)

    thickness = 6
    right_body_color = (0,69,255)
    left_body_color = (255,0,255)
    body_color = (255,255,0)
    if len(landmark_point) > 0:
        # left_eye
        if landmark_point[1][0] > visibility_th and landmark_point[2][0] > visibility_th:
            cv2.line(image, landmark_point[1][1], landmark_point[2][1], left_body_color, thickness)
        if landmark_point[2][0] > visibility_th and landmark_point[3][0] > visibility_th:
            cv2.line(image, landmark_point[2][1], landmark_point[3][1], left_body_color, thickness)
        # right_eye
        if landmark_point[4][0] > visibility_th and landmark_point[5][0] > visibility_th:
            cv2.line(image, landmark_point[4][1], landmark_point[5][1], right_body_color, thickness)
        if landmark_point[5][0] > visibility_th and landmark_point[6][0] > visibility_th:
            cv2.line(image, landmark_point[5][1], landmark_point[6][1], right_body_color, thickness)
        # mouth
        if landmark_point[9][0] > visibility_th and landmark_point[10][0] > visibility_th:
            cv2.line(image, landmark_point[9][1], landmark_point[10][1],(0, 0, 255), thickness)
        # shoulder
        if landmark_point[11][0] > visibility_th and landmark_point[12][0] > visibility_th:
            cv2.line(image, landmark_point[11][1], landmark_point[12][1], body_color, thickness)
        # left arm
        if landmark_point[11][0] > visibility_th and landmark_point[13][0] > visibility_th:
            cv2.line(image, landmark_point[11][1], landmark_point[13][1], left_body_color, thickness)
        if landmark_point[13][0] > visibility_th and landmark_point[15][0] > visibility_th:
            cv2.line(image, landmark_point[13][1], landmark_point[15][1], left_body_color, thickness)
        # right_arm
        if landmark_point[12][0] > visibility_th and landmark_point[14][0] > visibility_th:
            cv2.line(image, landmark_point[12][1], landmark_point[14][1], right_body_color, thickness)
        if landmark_point[14][0] > visibility_th and landmark_point[16][0] > visibility_th:
            cv2.line(image, landmark_point[14][1], landmark_point[16][1], right_body_color, thickness)
        # left hand
        if landmark_point[15][0] > visibility_th and landmark_point[17][0] > visibility_th:
            cv2.line(image, landmark_point[15][1], landmark_point[17][1], left_body_color, thickness)
        if landmark_point[17][0] > visibility_th and landmark_point[19][0] > visibility_th:
            cv2.line(image, landmark_point[17][1], landmark_point[19][1], left_body_color, thickness)
        if landmark_point[19][0] > visibility_th and landmark_point[21][0] > visibility_th:
            cv2.line(image, landmark_point[19][1], landmark_point[21][1], left_body_color, thickness)
        if landmark_point[21][0] > visibility_th and landmark_point[15][0] > visibility_th:
            cv2.line(image, landmark_point[21][1], landmark_point[15][1], left_body_color, thickness)
        # right hand
        if landmark_point[16][0] > visibility_th and landmark_point[18][0] > visibility_th:
            cv2.line(image, landmark_point[16][1], landmark_point[18][1], right_body_color, thickness)
        if landmark_point[18][0] > visibility_th and landmark_point[20][0] > visibility_th:
            cv2.line(image, landmark_point[18][1], landmark_point[20][1], right_body_color, thickness)
        if landmark_point[20][0] > visibility_th and landmark_point[22][0] > visibility_th:
            cv2.line(image, landmark_point[20][1], landmark_point[22][1], right_body_color, thickness)
        if landmark_point[22][0] > visibility_th and landmark_point[16][0] > visibility_th:
            cv2.line(image, landmark_point[22][1], landmark_point[16][1], right_body_color, thickness)
        # body
        if landmark_point[11][0] > visibility_th and landmark_point[23][0] > visibility_th:
            cv2.line(image, landmark_point[11][1], landmark_point[23][1], left_body_color, thickness)
        if landmark_point[12][0] > visibility_th and landmark_point[24][0] > visibility_th:
            cv2.line(image, landmark_point[12][1], landmark_point[24][1], right_body_color, thickness)
        if landmark_point[23][0] > visibility_th and landmark_point[24][0] > visibility_th:
            cv2.line(image, landmark_point[23][1], landmark_point[24][1], body_color, thickness)

        if len(landmark_point) > 25:
            # left foot
            if landmark_point[23][0] > visibility_th and landmark_point[25][0] > visibility_th:
                cv2.line(image, landmark_point[23][1], landmark_point[25][1], left_body_color, thickness)
            if landmark_point[25][0] > visibility_th and landmark_point[27][0] > visibility_th:
                cv2.line(image, landmark_point[25][1], landmark_point[27][1], left_body_color, thickness)
            if landmark_point[27][0] > visibility_th and landmark_point[29][0] > visibility_th:
                cv2.line(image, landmark_point[27][1], landmark_point[29][1], left_body_color, thickness)
            if landmark_point[29][0] > visibility_th and landmark_point[31][0] > visibility_th:
                cv2.line(image, landmark_point[29][1], landmark_point[31][1], left_body_color, thickness)

            # right foot
            if landmark_point[24][0] > visibility_th and landmark_point[26][0] > visibility_th:
                cv2.line(image, landmark_point[24][1], landmark_point[26][1], right_body_color, thickness)
            if landmark_point[26][0] > visibility_th and landmark_point[28][0] > visibility_th:
                cv2.line(image, landmark_point[26][1], landmark_point[28][1], right_body_color, thickness)
            if landmark_point[28][0] > visibility_th and landmark_point[30][0] > visibility_th:
                cv2.line(image, landmark_point[28][1], landmark_point[30][1], right_body_color, thickness)
            if landmark_point[30][0] > visibility_th and landmark_point[32][0] > visibility_th:
                cv2.line(image, landmark_point[30][1], landmark_point[32][1], right_body_color, thickness)

    return image

def plot_world_landmarks(plt, ax, landmarks, angle):
    landmark_point = []

    for index, landmark in enumerate(landmarks.landmark):
        landmark_point.append([landmark.visibility, (landmark.x, landmark.y, landmark.z)])

    face_index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    right_arm_index_list = [11, 13, 15, 17, 19, 21]
    left_arm_index_list = [12, 14, 16, 18, 20, 22]
    right_body_side_index_list = [11, 23, 25, 27, 29, 31]
    left_body_side_index_list = [12, 24, 26, 28, 30, 32]
    shoulder_index_list = [11, 12]
    waist_index_list = [23, 24]

    # face
    face_x, face_y, face_z = [], [], []
    for index in face_index_list:
        point = landmark_point[index][1]
        face_x.append(point[0])
        face_y.append(point[2])
        face_z.append(point[1] * (-1))

    # left arm
    right_arm_x, right_arm_y, right_arm_z = [], [], []
    for index in right_arm_index_list:
        point = landmark_point[index][1]
        right_arm_x.append(point[0])
        right_arm_y.append(point[2])
        right_arm_z.append(point[1] * (-1))

    # right arm
    left_arm_x, left_arm_y, left_arm_z = [], [], []
    for index in left_arm_index_list:
        point = landmark_point[index][1]
        left_arm_x.append(point[0])
        left_arm_y.append(point[2])
        left_arm_z.append(point[1] * (-1))

    # left body
    right_body_side_x, right_body_side_y, right_body_side_z = [], [], []
    for index in right_body_side_index_list:
        point = landmark_point[index][1]
        right_body_side_x.append(point[0])
        right_body_side_y.append(point[2])
        right_body_side_z.append(point[1] * (-1))

    # right body
    left_body_side_x, left_body_side_y, left_body_side_z = [], [], []
    for index in left_body_side_index_list:
        point = landmark_point[index][1]
        left_body_side_x.append(point[0])
        left_body_side_y.append(point[2])
        left_body_side_z.append(point[1] * (-1))

    # shoulder
    shoulder_x, shoulder_y, shoulder_z = [], [], []
    for index in shoulder_index_list:
        point = landmark_point[index][1]
        shoulder_x.append(point[0])
        shoulder_y.append(point[2])
        shoulder_z.append(point[1] * (-1))

    # waist
    waist_x, waist_y, waist_z = [], [], []
    for index in waist_index_list:
        point = landmark_point[index][1]
        waist_x.append(point[0])
        waist_y.append(point[2])
        waist_z.append(point[1] * (-1))
            
    ax.cla()
    ax.set_xlim3d(-1, 1)
    ax.set_ylim3d(-1, 1)
    ax.set_zlim3d(-1, 1)

    linewidth = 2
    ax.scatter(face_x, face_y, face_z, color='red')
    
    ax.plot(waist_x, waist_y, waist_z, lw = linewidth, color='aqua')
    ax.plot(shoulder_x, shoulder_y, shoulder_z, lw = linewidth, color='aqua')
    ax.plot(right_body_side_x, right_body_side_y, right_body_side_z, lw = linewidth, color='magenta')
    ax.plot(left_body_side_x, left_body_side_y, left_body_side_z, lw = linewidth, color='orangered')
    ax.plot(right_arm_x, right_arm_y, right_arm_z, lw = linewidth, color='magenta')
    ax.plot(left_arm_x, left_arm_y, left_arm_z, lw = linewidth, color='orangered')
    
    ax.view_init(elev=20, azim=angle)
    plot_3d_placeholder.pyplot(fig, clear_figure= False)

    return