





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Row  {

    private int RowIndex;





    private List<spreadsheet_Cell> spreadsheet_cells;




    private spreadsheet_Sheet spreadsheet_sheet;




    private spreadsheet_Cell spreadsheet_cell;




    private spreadsheet_Sheet spreadsheet_sheet;


    public spreadsheet_Row(
        int RowIndex    ) {
        this.RowIndex = RowIndex;
        this.spreadsheet_cells = new ArrayList<>();
    }

    public spreadsheet_Row(
        int RowIndex        ArrayList<spreadsheet_Cell> spreadsheet_cells    ) {
        this.RowIndex = RowIndex;
        this.spreadsheet_cells = spreadsheet_cells;
    }

    public int getRowindex() {
        return RowIndex;
    }

    public void setRowindex(int RowIndex) {
        this.RowIndex = RowIndex;
    }

    public List<spreadsheet_Cell> getSpreadsheet_cells() {
        return spreadsheet_cells;
    }

    public void addSpreadsheet_cell(Spreadsheet_cell spreadsheet_cell) {
        this.spreadsheet_cells.add(spreadsheet_cell);
    }
    public spreadsheet_Sheet getSpreadsheet_sheet() {
        return spreadsheet_sheet;
    }

    public void setSpreadsheet_sheet(spreadsheet_Sheet spreadsheet_sheet) {
        this.spreadsheet_sheet = spreadsheet_sheet;
    }
    public spreadsheet_Cell getSpreadsheet_cell() {
        return spreadsheet_cell;
    }

    public void setSpreadsheet_cell(spreadsheet_Cell spreadsheet_cell) {
        this.spreadsheet_cell = spreadsheet_cell;
    }
    public spreadsheet_Sheet getSpreadsheet_sheet() {
        return spreadsheet_sheet;
    }

    public void setSpreadsheet_sheet(spreadsheet_Sheet spreadsheet_sheet) {
        this.spreadsheet_sheet = spreadsheet_sheet;
    }

}