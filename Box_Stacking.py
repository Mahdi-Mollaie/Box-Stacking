def create_box():
    global num
    num = int(input("How many boxes do you have?\n"))
    boxes = []
    for _ in range(num):
        print("Enter their dimensions :\n Lenght, Width, Height")
        lenght = int(input())
        width = int(input())
        height = int(input())
        boxes.append([lenght,width,height])
    print('#' * 100)
    print(f'Your boxes are : \n{boxes}')
    print('#' * 100)
    return boxes

def rotate_boxes(boxes):
    rotation = []
    for f in range (3 * num):
        rotation.append([0, 0, 0])

    index = 0
 
    for i in range(num):
        rotation[index][2] = boxes[i][2]
        rotation[index][0] = max(boxes[i][0], boxes[i][1])
        rotation[index][1] = min(boxes[i][0], boxes[i][1])
        index += 1
        rotation[index][2] = boxes[i][1]
        rotation[index][0] = max(boxes[i][2], boxes[i][0])
        rotation[index][1] = min(boxes[i][2], boxes[i][0])
        index += 1
        rotation[index][2] = boxes[i][0]
        rotation[index][0] = max(boxes[i][2], boxes[i][1])
        rotation[index][1] = min(boxes[i][2], boxes[i][1])
        index += 1

    rotation.sort(reverse = True)
    return rotation


def find_max_height(sorted_boxes):
    max_height = [0]  * len(sorted_boxes)
    for i in range(len(sorted_boxes)):
        for j in range(i):
            if (sorted_boxes[i][0] < sorted_boxes[j][0] and
                    sorted_boxes[i][1] < sorted_boxes[j][1]):
                max_height[i] = max(max_height[i], max_height[j])
        max_height[i] += sorted_boxes[i][2]
        
    print(sorted_boxes[i])   
    return max(max_height)

boxes = create_box()
rotated = rotate_boxes(boxes)
rotated.sort(key=lambda x: (x[0] * x[1]), reverse=True)
final = find_max_height(rotated)
print(f"The maximum height is : {final}")