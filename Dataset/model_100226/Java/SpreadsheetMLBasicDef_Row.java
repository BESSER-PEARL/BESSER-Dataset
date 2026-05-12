





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_Row extends ColOrRowElement {

    private String autoFitHeight;
    private String height;





    private Table table;




    private List<Cell> cells;


    public SpreadsheetMLBasicDef_Row(
        String autoFitHeight,        String height    ) {
        super(
        );
        this.autoFitHeight = autoFitHeight;
        this.height = height;
        this.cells = new ArrayList<>();
    }

    public SpreadsheetMLBasicDef_Row(
        String autoFitHeight,        String height        ArrayList<Cell> cells    ) {
        this.autoFitHeight = autoFitHeight;
        this.height = height;
        this.cells = cells;
    }

    public String getAutofitheight() {
        return autoFitHeight;
    }

    public void setAutofitheight(String autoFitHeight) {
        this.autoFitHeight = autoFitHeight;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public List<Cell> getCells() {
        return cells;
    }

    public void addCell(Cell cell) {
        this.cells.add(cell);
    }

}