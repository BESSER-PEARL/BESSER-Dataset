





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorksheetOpt_Table extends StyledElement {

    private String leftCell;
    private String topCell;
    private String fullRows;
    private String defaultRowHeight;
    private String expandedColumnCount;
    private String expandedRowCount;
    private String defaultColumnWidth;
    private String fullColumns;





    private List<Row> rows;




    private Worksheet worksheet;


    public SpreadsheetMLWorksheetOpt_Table(
        String leftCell,        String topCell,        String fullRows,        String defaultRowHeight,        String expandedColumnCount,        String expandedRowCount,        String defaultColumnWidth,        String fullColumns    ) {
        super(
        );
        this.leftCell = leftCell;
        this.topCell = topCell;
        this.fullRows = fullRows;
        this.defaultRowHeight = defaultRowHeight;
        this.expandedColumnCount = expandedColumnCount;
        this.expandedRowCount = expandedRowCount;
        this.defaultColumnWidth = defaultColumnWidth;
        this.fullColumns = fullColumns;
        this.rows = new ArrayList<>();
    }

    public SpreadsheetMLWorksheetOpt_Table(
        String leftCell,        String topCell,        String fullRows,        String defaultRowHeight,        String expandedColumnCount,        String expandedRowCount,        String defaultColumnWidth,        String fullColumns        ArrayList<Row> rows    ) {
        this.leftCell = leftCell;
        this.topCell = topCell;
        this.fullRows = fullRows;
        this.defaultRowHeight = defaultRowHeight;
        this.expandedColumnCount = expandedColumnCount;
        this.expandedRowCount = expandedRowCount;
        this.defaultColumnWidth = defaultColumnWidth;
        this.fullColumns = fullColumns;
        this.rows = rows;
    }

    public String getLeftcell() {
        return leftCell;
    }

    public void setLeftcell(String leftCell) {
        this.leftCell = leftCell;
    }
    public String getTopcell() {
        return topCell;
    }

    public void setTopcell(String topCell) {
        this.topCell = topCell;
    }
    public String getFullrows() {
        return fullRows;
    }

    public void setFullrows(String fullRows) {
        this.fullRows = fullRows;
    }
    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
    }
    public String getExpandedcolumncount() {
        return expandedColumnCount;
    }

    public void setExpandedcolumncount(String expandedColumnCount) {
        this.expandedColumnCount = expandedColumnCount;
    }
    public String getExpandedrowcount() {
        return expandedRowCount;
    }

    public void setExpandedrowcount(String expandedRowCount) {
        this.expandedRowCount = expandedRowCount;
    }
    public String getDefaultcolumnwidth() {
        return defaultColumnWidth;
    }

    public void setDefaultcolumnwidth(String defaultColumnWidth) {
        this.defaultColumnWidth = defaultColumnWidth;
    }
    public String getFullcolumns() {
        return fullColumns;
    }

    public void setFullcolumns(String fullColumns) {
        this.fullColumns = fullColumns;
    }

    public List<Row> getRows() {
        return rows;
    }

    public void addRow(Row row) {
        this.rows.add(row);
    }
    public Worksheet getWorksheet() {
        return worksheet;
    }

    public void setWorksheet(Worksheet worksheet) {
        this.worksheet = worksheet;
    }

}