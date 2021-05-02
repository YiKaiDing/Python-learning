import pandas as pd
import itertools
import math
import tkinter as tk
from tkinter.filedialog import askopenfilename


def dollar_max_app():

    def import_file():
        """Import a CSV file."""
        global input_df_ascending, value_list
        file_name = askopenfilename(
            filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx'))]#[("CSV Files", "*.CSV"), ("All Files", "*.*")]
        )
        window.title(f"Dollar Max Export - {file_name}")

        if file_name:
            if file_name.endswith('.csv'):
                input_df = pd.read_csv(file_name)
                input_df["Person Value"] = input_df["Person Value"].replace({'\$': '', ',': ''}, regex=True).astype(float)
                input_df_ascending = input_df.sort_values(by='Person Value', ascending=True)

                value_df = input_df.loc[:, ['List ID', 'Person Value']].sort_values(
                    by='Person Value', ascending=False).reset_index(drop=True)
                value_list = list(value_df['Person Value'])
                value_list = [int(value) for value in value_list]

            else:
                input_df = pd.read_excel(file_name)
                input_df_ascending = input_df.sort_values(by='Person Value', ascending=True)
                value_df = input_df.loc[:, ['List ID', 'Person Value']].sort_values(by='Person Value', ascending=False).reset_index(
                    drop=True)
                value_list = list(value_df['Person Value'])
        return input_df_ascending, value_list


    def choose_k_from_n(n, k):
        if k == 0:
            return 1
        elif n < k:
            return 0
        elif n == k:
            return 1
        else:
            return int(math.factorial(n) / math.factorial(n - k) / math.factorial(k))

    def combine_app(array, d_max, row):
        if row == 0:
            return 1
        elif len(array) < row:
            return 0
        elif len(array) == row:
            if sum(array) > d_max:
                return 0
            else:
                return 1
        else:
            if array[0] > d_max:
                array.remove(array[0])
                return combine_app(array, d_max, row)

            elif array[0] <= d_max / row:
                return choose_k_from_n(len(array), row)

            else:
                new_d_max = d_max - array[0]
                return combine_app(array[1:], d_max, row) + combine_app(array[1:], new_d_max, row - 1)

    def group_export(array, d_max, row, groups_export):
        group_list = list(array.index)
        group_indices = itertools.combinations(group_list, row_num)

        export_groups = pd.DataFrame([])
        group_num = 0

        if possibility == 0:
            return "No output!"

        if groups_export > possibility:
            return "Error, the total group possibility is smaller than maximum possible group number you input!"
        else:
            for group_index in group_indices:
                sliced_group = pd.DataFrame(array, index=group_index)
                if sliced_group['Person Value'].sum() <= d_max:
                    group_num += 1
                    sliced_group.insert(loc=0, column='Group', value=group_num)
                    sliced_group = sliced_group.append(pd.Series(), ignore_index=True)
                    export_groups = export_groups.append(sliced_group)

                if group_num % export_per_time == 0 and group_num != 0:
                    print(sliced_group)

                    insert_col(export_groups, more_cols)

                    filename = export_data + str(group_num // export_per_time) + '.csv'
                    export_groups.to_csv(filename, index=False)
                    export_groups = pd.DataFrame([])

                if group_num >= groups_export:
                    if group_num % export_per_time == 0:
                        break
                    else:
                        insert_col(export_groups, more_cols)
                        filename = export_data + str(group_num // export_per_time + 1) + '.csv'
                        export_groups.to_csv(filename, index=False)
                        break

            return "Dollar max script done!"

    def simple_app():


        export_per_time = input('Please enter the maximum group number you want to export in a single excel file such as 5000:')
        export_per_time = int(export_per_time)

        group_indices = itertools.combinations(group_list, int(row_num))

        export_list = []
        export_groups = pd.DataFrame(export_list)
        group_num = 0

        for group_index in group_indices:
            group_num += 1
            sliced_group = pd.DataFrame(original_data, index=group_index)
            sliced_group.insert(loc=0, column='Group', value=group_num)
            sliced_group = sliced_group.append(pd.Series(), ignore_index=True)
            export_groups = export_groups.append(sliced_group)

            if group_num % export_per_time == 0 and group_num != 0:
                filename = export_data + str(group_num // export_per_time) + '.csv'
                export_groups.to_csv(filename, index=False)
                export_groups = pd.DataFrame([])

        filename = export_data + str(group_num // export_per_time + 1) + '.csv'
        export_groups.to_csv(filename, index=False)
        print("Simple combination scripts done!")


    def calculate_combination():
        dollar_max = ent_dollar_max.get()
        row_num = ent_row_num.get()


        if A:
            total_possibility["text"] = choose_k_from_n(len(value_list), row_num)
        else:
            total_possibility["text"] = combine_app(value_list, dollar_max, row_num)


    def export_file ():
        export_number = ent_export_number.get()
        input_df_ascending, value_list = import_file()
        dollar_max = ent_dollar_max.get()
        row_num = ent_row_num.get()

        message = group_export(input_df_ascending, dollar_max, row_num, export_number)
        print(message)



    window = tk.Tk()
    window.title("Dollar Max")

    window.rowconfigure(5, minsize=400, weight=1)
    window.columnconfigure(3, minsize=400, weight=1)

    lbl_dollar_max = tk.Label(master=window, text="Dollar Max", font=('calibre', 10, 'bold'))
    ent_dollar_max = tk.Entry(master=window, width=10)
    lbl_dollar_max.grid(row=0, column=0, sticky="w")
    ent_dollar_max.grid(row=0, column=1)

    lbl_row_num = tk.Label(master=window, text="Row Number", font=('calibre', 10, 'bold'))
    ent_row_num = tk.Entry(master=window, width=10)
    lbl_row_num.grid(row=0, column=2, sticky="w")
    ent_row_num.grid(row=0, column=3)



    lbl_choice = tk.Label(master=window, text="Export Choice", font=('calibre', 10, 'bold'))
    lbl_choice.grid(row=1, column=0, sticky="ew")

    var = tk.IntVar()
    radio_simple_app = tk.Radiobutton(window, text="Simple Combination", variable=var, value=1, command=simple_app)
    radio_combine_app = tk.Radiobutton(window, text="Dollar Max", variable=var, value=2, command=combine_app)
    radio_simple_app.grid(row=1, column=1, sticky="ew")
    radio_combine_app.grid(row=1, column=2, sticky="ew")

    total_possibility_text = tk.Label(master=window, text="Total Possibility is:")
    total_possibility_text.grid(row=2, column=0)
    total_possibility = tk.Label(master=window, text="0")
    total_possibility.grid(row=2, column=1)

    export_number_text = tk.Label(master=window, text="Export groups")
    export_number_text.grid(row=2, column=2)
    ent_export_number = tk.Entry(master=window, width=10)
    ent_export_number.grid(row=2, column=3)

    btn_open = tk.Button(window, text="Import", command=import_file)
    btn_open.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    btn_open = tk.Button(window, text="Calculate", command=calculate_combination)
    btn_open.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

    btn_open = tk.Button(window, text="Export", command=export_file)
    btn_open.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

    window.mainloop()


def main():
    dollar_max_app()


if __name__ == '__main__':
    main()


