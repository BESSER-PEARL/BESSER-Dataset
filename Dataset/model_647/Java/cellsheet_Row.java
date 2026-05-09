





import java.util.List;
import java.util.ArrayList;

public class cellsheet_Row extends HasId, HasA1 {

    private int rowIndex;





    private cellsheet_Sheet cellsheet_sheet;




    private cellsheet_Sheet cellsheet_sheet;




    private cellsheet_Cell cellsheet_cell;




    private List<cellsheet_Cell> cellsheet_cells;


    public cellsheet_Row(
        int rowIndex    ) {
        super(
        );
        this.rowIndex = rowIndex;
        this.cellsheet_cells = new ArrayList<>();
    }

    public cellsheet_Row(
        int rowIndex        ArrayList<cellsheet_Cell> cellsheet_cells    ) {
        this.rowIndex = rowIndex;
        this.cellsheet_cells = cellsheet_cells;
    }

    public int getRowindex() {
        return rowIndex;
    }

    public void setRowindex(int rowIndex) {
        this.rowIndex = rowIndex;
    }

    public cellsheet_Sheet getCellsheet_sheet() {
        return cellsheet_sheet;
    }

    public void setCellsheet_sheet(cellsheet_Sheet cellsheet_sheet) {
        this.cellsheet_sheet = cellsheet_sheet;
    }
    public cellsheet_Sheet getCellsheet_sheet() {
        return cellsheet_sheet;
    }

    public void setCellsheet_sheet(cellsheet_Sheet cellsheet_sheet) {
        this.cellsheet_sheet = cellsheet_sheet;
    }
    public cellsheet_Cell getCellsheet_cell() {
        return cellsheet_cell;
    }

    public void setCellsheet_cell(cellsheet_Cell cellsheet_cell) {
        this.cellsheet_cell = cellsheet_cell;
    }
    public List<cellsheet_Cell> getCellsheet_cells() {
        return cellsheet_cells;
    }

    public void addCellsheet_cell(Cellsheet_cell cellsheet_cell) {
        this.cellsheet_cells.add(cellsheet_cell);
    }

}