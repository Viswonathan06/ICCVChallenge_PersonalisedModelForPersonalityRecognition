from typing import final
import pandas as pd

path_to_fb = "/mnt/Results/fb_pred.csv"

path_to_textual = "/mnt/Results/alltextual_results.csv"

df_fb = pd.read_csv(path_to_fb)
df_textual = pd.read_csv(path_to_textual, header=None)

# print(df_fb.index)
# print(df_textual.index)

df_fb = df_fb.reset_index(drop= True)

df_fb = df_fb.drop(["Unnamed: 0","minute"], axis = 1)
mean_df_fb = df_fb.groupby(['ID_y'], as_index=False).mean()
mean_df_fb.columns = [0, 1, 2, 3, 4, 5]
# print(mean_df_fb.head())

# print("textual")
# print(df_textual.head())
df_textual.drop(df_textual.columns[1], axis = 1, inplace = True)
# print("After dropping:")
# print(df_textual.head())
df_textual.columns = [0, 1, 2, 3, 4, 5]
mean_df_text = df_textual.groupby(df_textual.columns[0], as_index=False).mean()
# print(mean_df_text.head(20))

final_pred = mean_df_text.append(mean_df_fb)
final_pred = final_pred.groupby(final_pred.columns[0], as_index=False).mean()
final_pred.columns = ["Participant ID",	"OPENMINDEDNESS_Z",	"CONSCIENTIOUSNESS_Z",	"EXTRAVERSION_Z",	"AGREEABLENESS_Z",	"NEGATIVEEMOTIONALITY_Z"]
print(final_pred.head(20))
final_pred.to_csv("./final_predictions.csv")
