Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
   - Formula: $C = (F - 32) \times \frac{5}{9}$

---

Task 2. Create a custom function that takes two arguments: a number and a power. Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.

---

Task 3. Solve the system of equations using `numpy`:

$$
\begin{cases}
4x + 5y + 6z = 7 \\
3x - y + z = 4 \\
2x + y - 2z = 5
\end{cases}
$$

---

Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

$$
\begin{cases}
10I_1 - 2I_2 + 3I_3 = 12 \\
-2I_1 + 8I_2 - I_3 = -5 \\
3I_1 - I_2 + 6I_3 = 15
\end{cases}
$$

---


**Image Manipulation with NumPy and PIL**

Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

**Instructions:**

1. **Flip the Image**:
   - Flip the image horizontally and vertically (left-to-right and up-to-down).

2. **Add Random Noise**:
   - Add random noise to the image.

3. **Brighten Channels**:
   - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

4. **Apply a Mask**:
   - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

**Requirements:**
- Use the **PIL** module onyl to:
  - Read the image.
  - Convert numpy array to image.
  - Save the modified image back to a file.
- Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


**Bonus Challenge**:
- Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.

--- 
