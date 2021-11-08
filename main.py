def medians(nums1, nums2):
    nums = nums1 + nums2
    sorted_nums = sorted(nums)
    print(sorted_nums)
    nums_length = len(sorted_nums)
    middle_index = (nums_length - 1) // 2

    if nums_length % 2 != 0:
        return sorted_nums[middle_index]
    else:
        return (sorted_nums[middle_index] + sorted_nums[middle_index + 1]) / 2