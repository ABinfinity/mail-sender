int* sortArray(int* arr, int len)
{
	int i, max, location, j, temp;
	for (i = 0; i < len; ++i)
	{
		/* code */
		max = arr[i];
		location = i;
		for (j= i; j < len; ++j)
		{
			/* code */
			if (max<arr[j])
			{
				/* code */
				max = arr[j];
				location = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[location];
		arr[location] = temp;
	}
	return arr;

}