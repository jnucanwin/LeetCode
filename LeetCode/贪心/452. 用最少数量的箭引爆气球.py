class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        根据每个坐标的右端点排序
        遍历，若左端点大于上一个的右端点，则+1（91.03）
        注:用lambda函数进行不同关键字排序
        """
        if not points:
            return 0
        points.sort(key=lambda p:p[1])
        shot_num = 1
        shot= points[0][1]
        for i in range(len(points)):

            if points[i][0] > shot:

                shot_num += 1
                shot = points[i][1]
        return shot_num
