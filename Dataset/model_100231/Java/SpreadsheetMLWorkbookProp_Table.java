





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_Table extends StyledElement {

    private String defaultRowHeight;
    private String fullRows;
    private String expandedColumnCount;
    private String topCell;
    private String expandedRowCount;
    private String leftCell;
    private String fullColumns;
    private String defaultColumnWidth;





    private List<Row> rows;




    private Worksheet worksheet;


    public SpreadsheetMLWorkbookProp_Table(
        String defaultRowHeight,        String fullRows,        String expandedColumnCount,        String topCell,        String expandedRowCount,        String leftCell,        String fullColumns,        String defaultColumnWidth    ) {
        super(
        );
        this.defaultRowHeight = defaultRowHeight;
        this.fullRows = fullRows;
        this.expandedColumnCount = expandedColumnCount;
        this.topCell = topCell;
        this.expandedRowCount = expandedRowCount;
        this.leftCell = leftCell;
        this.fullColumns = fullColumns;
        this.defaultColumnWidth = defaultColumnWidth;
        this.rows = new ArrayList<>();
    }

    public SpreadsheetMLWorkbookProp_Table(
        String defaultRowHeight,        String fullRows,        String expandedColumnCount,        String topCell,        String expandedRowCount,        String leftCell,        String fullColumns,        String defaultColumnWidth        ArrayList<Row> rows    ) {
        this.defaultRowHeight = defaultRowHeight;
        this.fullRows = fullRows;
        this.expandedColumnCount = expandedColumnCount;
        this.topCell = topCell;
        this.expandedRowCount = expandedRowCount;
        this.leftCell = leftCell;
        this.fullColumns = fullColumns;
        this.defaultColumnWidth = defaultColumnWidth;
        this.rows = rows;
    }

    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
    }
    public String getFullrows() {
        return fullRows;
    }

    public void setFullrows(String fullRows) {
        this.fullRows = fullRows;
    }
    public String getExpandedcolumncount() {
        return expandedColumnCount;
    }

    public void setExpandedcolumncount(String expandedColumnCount) {
        this.expandedColumnCount = expandedColumnCount;
    }
    public String getTopcell() {
        return topCell;
    }

    public void setTopcell(String topCell) {
        this.topCell = topCell;
    }
    public String getExpandedrowcount() {
        return expandedRowCount;
    }

    public void setExpandedrowcount(String expandedRowCount) {
        this.expandedRowCount = expandedRowCount;
    }
    public String getLeftcell() {
        return leftCell;
    }

    public void setLeftcell(String leftCell) {
        this.leftCell = leftCell;
    }
    public String getFullcolumns() {
        return fullColumns;
    }

    public void setFullcolumns(String fullColumns) {
        this.fullColumns = fullColumns;
    }
    public String getDefaultcolumnwidth() {
        return defaultColumnWidth;
    }

    public void setDefaultcolumnwidth(String defaultColumnWidth) {
        this.defaultColumnWidth = defaultColumnWidth;
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