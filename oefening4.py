def countTargetPairs(nums, target):
    aantalPairs = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                aantalPairs = aantalPairs + 1
    return aantalPairs

# 1e voorbeeld
print(countTargetPairs([-1, 1, 2, 3, 1], 2))


