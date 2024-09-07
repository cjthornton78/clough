# from datetime import datetime
from get_raw_data_from_xlsx_sheets import get_current_time_string  # I should probably put this in its own module

TABLE_INSERTION_POINT = '<!-- #CLOUGH -->'  # The key string which will be replaced with the table data from Excel


def split_template(template_file_path):
    with open(template_file_path, 'r') as template_file:
        template_html = template_file.read()

    # Split the template_html into two parts using the split method
    template_top, template_tail = template_html.split(TABLE_INSERTION_POINT, 1)
    # The `1` in the split method ensures that the string is split at the first occurrence of the marker

    return template_top, template_tail


def insert_table_into_template(template_file, table_strings):
    current_time = get_current_time_string()
    output_file_path = f'test_data/output/cloughtest_output.html'  # {current_time}_  TODO - add this prefix back in

    sheet_key_iterator = iter(table_strings)
    first_sheet_in_table = next(sheet_key_iterator)

    # Need to process first sheet separately to create tables_to_insert for later additions from other sheets
    tables_to_insert = table_strings[first_sheet_in_table]
    html_template_top, html_template_tail = split_template(template_file)
    workbook_tabs_html = f'''\n\n<div class="tabs">\n
    <button class="tab-link active" onclick="showSheet(event, '{first_sheet_in_table}')">{first_sheet_in_table}</button>\n'''

    # Now use the iterator to add sheets after the first one, if there are any
    if len(table_strings) > 1:
        try:
            for sheet_name in sheet_key_iterator:
                tables_to_insert += f'\n\n{table_strings[sheet_name]}'
                workbook_tabs_html += f'''<button class="tab-link" onclick="showSheet(event, '{sheet_name}')">{sheet_name}</button>\n'''
        except StopIteration:
            print('Error: no more sheets left')  # Should be unreachable
    
    tab_offset = '\t\t'  # TODO - Set programmatically
    full_html = html_template_top + f'{tab_offset}<div class="spreadsheet-workbook">\n' + tables_to_insert + f'{tab_offset}</div>\n' + workbook_tabs_html + html_template_tail

    with open(output_file_path, 'w') as output_file:
        output_file.write(full_html)

        output_file.close()



if __name__ == '__main__':
    print('   --- START ---')
    
    html_template_file = r'test_data/cloughtest_template.html'
    all_table_strings = {'Sheet1': '''<table class="clough " id="Sheet1" style="width:80%">\n\t<caption class="">Converted from Excel by Clough</caption>\n\t<thead class="">\n\t\t<tr class="">\n\t\t\t<th class="clough-column-letters"></th>\n\t\t\t<th class="clough-column-letters">A</th>\n\t\t\t<th class="clough-column-letters">B</th>\n\t\t</tr>\n\t</thead>\n\n\t<tbody class="">\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">1</td>\n\t\t\t<td class="clough-align-center clough-font-bold">Date</td>\n\t\t\t<td class="clough-align-center clough-font-bold">Rainfall (mm)</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">2</td>\n\t\t\t<td class="clough-align-none">01-Aug-24</td>\n\t\t\t<td class="clough-align-none">5.2</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">3</td>\n\t\t\t<td class="clough-align-none">02-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">4</td>\n\t\t\t<td class="clough-align-none">03-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic">12.4</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">5</td>\n\t\t\t<td class="clough-align-none">04-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic">3.8</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">6</td>\n\t\t\t<td class="clough-align-none">05-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-underline">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">7</td>\n\t\t\t<td class="clough-align-none">06-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-underline">18.7</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">8</td>\n\t\t\t<td class="clough-align-none">07-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-italic clough-font-underline">6.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">9</td>\n\t\t\t<td class="clough-align-none">08-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">10</td>\n\t\t\t<td class="clough-align-none">09-Aug-24</td>\n\t\t\t<td class="clough-align-center">2.9</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">11</td>\n\t\t\t<td class="clough-align-none">10-Aug-24</td>\n\t\t\t<td class="clough-align-left">14.2</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">12</td>\n\t\t\t<td class="clough-align-none">11-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">13</td>\n\t\t\t<td class="clough-align-none">12-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-italic">4.5999999999999996</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">14</td>\n\t\t\t<td class="clough-align-none">13-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic clough-font-underline">9.1</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">15</td>\n\t\t\t<td class="clough-align-none">14-Aug-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-underline">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">16</td>\n\t\t\t<td class="clough-align-none">15-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">17</td>\n\t\t\t<td class="clough-align-none">16-Aug-24</td>\n\t\t\t<td class="clough-align-none">23.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">18</td>\n\t\t\t<td class="clough-align-none">17-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">19</td>\n\t\t\t<td class="clough-align-none">18-Aug-24</td>\n\t\t\t<td class="clough-align-none">1.5</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">20</td>\n\t\t\t<td class="clough-align-none">19-Aug-24</td>\n\t\t\t<td class="clough-align-none">7.8</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">21</td>\n\t\t\t<td class="clough-align-none">20-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">22</td>\n\t\t\t<td 
class="clough-align-none">21-Aug-24</td>\n\t\t\t<td class="clough-align-none">15.6</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">23</td>\n\t\t\t<td class="clough-align-none">22-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">24</td>\n\t\t\t<td class="clough-align-none">23-Aug-24</td>\n\t\t\t<td class="clough-align-none">8.1999999999999993</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">25</td>\n\t\t\t<td class="clough-align-none">24-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">26</td>\n\t\t\t<td class="clough-align-none">25-Aug-24</td>\n\t\t\t<td class="clough-align-none">13.7</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">27</td>\n\t\t\t<td class="clough-align-none">26-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">28</td>\n\t\t\t<td class="clough-align-none">27-Aug-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">29</td>\n\t\t\t<td class="clough-align-none">28-Aug-24</td>\n\t\t\t<td class="clough-align-none">19.399999999999999</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">30</td>\n\t\t\t<td class="clough-align-none">29-Aug-24</td>\n\t\t\t<td class="clough-align-none">13.5</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">31</td>\n\t\t\t<td class="clough-align-none">30-Aug-24</td>\n\t\t\t<td class="clough-align-none">11.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">32</td>\n\t\t\t<td class="clough-align-none">31-Aug-24</td>\n\t\t\t<td class="clough-align-none">Forgot this one</td>\n\t\t</tr>\n\t</tbody>\n\n\t<tfoot class="">\n\t</tfoot>\n\n</table>\n''',
                        'Sheet2': '''<table class="clough " id="Sheet2" style="width:80%">\n\t<caption class="">Converted from Excel by Clough</caption>\n\t<thead class="">\n\t\t<tr class="">\n\t\t\t<th class="clough-column-letters"></th>\n\t\t\t<th class="clough-column-letters">A</th>\n\t\t\t<th class="clough-column-letters">B</th>\n\t\t</tr>\n\t</thead>\n\n\t<tbody class="">\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">1</td>\n\t\t\t<td class="clough-align-center clough-font-bold">Date</td>\n\t\t\t<td class="clough-align-center clough-font-bold">Rainfall (mm)</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">2</td>\n\t\t\t<td class="clough-align-none">01-Sep-24</td>\n\t\t\t<td class="clough-align-none">5.2</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">3</td>\n\t\t\t<td class="clough-align-none">02-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">4</td>\n\t\t\t<td class="clough-align-none">03-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic">12.4</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">5</td>\n\t\t\t<td class="clough-align-none">04-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic">3.8</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">6</td>\n\t\t\t<td class="clough-align-none">05-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-underline">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">7</td>\n\t\t\t<td class="clough-align-none">06-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-underline">18.7</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">8</td>\n\t\t\t<td class="clough-align-none">07-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-italic clough-font-underline">6.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">9</td>\n\t\t\t<td class="clough-align-none">08-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">10</td>\n\t\t\t<td class="clough-align-none">09-Sep-24</td>\n\t\t\t<td class="clough-align-center">2.9</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td 
class="clough-row-numbers">11</td>\n\t\t\t<td class="clough-align-none">10-Sep-24</td>\n\t\t\t<td class="clough-align-left">14.2</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">12</td>\n\t\t\t<td class="clough-align-none">11-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">13</td>\n\t\t\t<td class="clough-align-none">12-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-italic">4.5999999999999996</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">14</td>\n\t\t\t<td class="clough-align-none">13-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-italic clough-font-underline">9.1</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">15</td>\n\t\t\t<td class="clough-align-none">14-Sep-24</td>\n\t\t\t<td class="clough-align-none clough-font-bold clough-font-underline">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">16</td>\n\t\t\t<td class="clough-align-none">15-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">17</td>\n\t\t\t<td class="clough-align-none">16-Sep-24</td>\n\t\t\t<td class="clough-align-none">23.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">18</td>\n\t\t\t<td class="clough-align-none">17-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">19</td>\n\t\t\t<td class="clough-align-none">18-Sep-24</td>\n\t\t\t<td class="clough-align-none">1.5</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">20</td>\n\t\t\t<td class="clough-align-none">19-Sep-24</td>\n\t\t\t<td class="clough-align-none">7.8</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">21</td>\n\t\t\t<td class="clough-align-none">20-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">22</td>\n\t\t\t<td class="clough-align-none">21-Sep-24</td>\n\t\t\t<td class="clough-align-none">15.6</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">23</td>\n\t\t\t<td class="clough-align-none">22-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">24</td>\n\t\t\t<td class="clough-align-none">23-Sep-24</td>\n\t\t\t<td 
class="clough-align-none">8.1999999999999993</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">25</td>\n\t\t\t<td class="clough-align-none">24-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">26</td>\n\t\t\t<td class="clough-align-none">25-Sep-24</td>\n\t\t\t<td class="clough-align-none">13.7</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td 
class="clough-row-numbers">27</td>\n\t\t\t<td class="clough-align-none">26-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">28</td>\n\t\t\t<td class="clough-align-none">27-Sep-24</td>\n\t\t\t<td class="clough-align-none">0</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">29</td>\n\t\t\t<td class="clough-align-none">28-Sep-24</td>\n\t\t\t<td class="clough-align-none">19.399999999999999</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">30</td>\n\t\t\t<td class="clough-align-none">29-Sep-24</td>\n\t\t\t<td class="clough-align-none">13.5</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">31</td>\n\t\t\t<td class="clough-align-none">30-Sep-24</td>\n\t\t\t<td class="clough-align-none">11.3</td>\n\t\t</tr>\n\t\t<tr class="">\n\t\t\t<td class="clough-row-numbers">32</td>\n\t\t\t<td class="clough-align-none"></td>\n\t\t</tr>\n\t</tbody>\n\n\t<tfoot class="">\n\t</tfoot>\n\n</table>\n'''}

    insert_table_into_template(html_template_file, all_table_strings)

    print('   --- END ---')