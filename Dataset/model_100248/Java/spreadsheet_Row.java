





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Row  {






    private List<spreadsheet_Cell> spreadsheet_cells;




    private spreadsheet_Table spreadsheet_table;


    public spreadsheet_Row(
    ) {
        this.spreadsheet_cells = new ArrayList<>();
    }

    public spreadsheet_Row(
        ArrayList<spreadsheet_Cell> spreadsheet_cells    ) {
        this.spreadsheet_cells = spreadsheet_cells;
    }


    public List<spreadsheet_Cell> getSpreadsheet_cells() {
        return spreadsheet_cells;
    }

    public void addSpreadsheet_cell(Spreadsheet_cell spreadsheet_cell) {
        this.spreadsheet_cells.add(spreadsheet_cell);
    }
    public spreadsheet_Table getSpreadsheet_table() {
        return spreadsheet_table;
    }

    public void setSpreadsheet_table(spreadsheet_Table spreadsheet_table) {
        this.spreadsheet_table = spreadsheet_table;
    }

}