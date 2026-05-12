





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_Table extends StyledElement {

    private String fullColumns;
    private String defaultRowHeight;
    private String topCell;
    private String fullRows;
    private String leftCell;
    private String defaultColumnWidth;
    private String expandedRowCount;
    private String expandedColumnCount;





    private Worksheet worksheet;


    public SpreadsheetMLStyles_Table(
        String fullColumns,        String defaultRowHeight,        String topCell,        String fullRows,        String leftCell,        String defaultColumnWidth,        String expandedRowCount,        String expandedColumnCount    ) {
        super(
        );
        this.fullColumns = fullColumns;
        this.defaultRowHeight = defaultRowHeight;
        this.topCell = topCell;
        this.fullRows = fullRows;
        this.leftCell = leftCell;
        this.defaultColumnWidth = defaultColumnWidth;
        this.expandedRowCount = expandedRowCount;
        this.expandedColumnCount = expandedColumnCount;
    }


    public String getFullcolumns() {
        return fullColumns;
    }

    public void setFullcolumns(String fullColumns) {
        this.fullColumns = fullColumns;
    }
    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
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
    public String getLeftcell() {
        return leftCell;
    }

    public void setLeftcell(String leftCell) {
        this.leftCell = leftCell;
    }
    public String getDefaultcolumnwidth() {
        return defaultColumnWidth;
    }

    public void setDefaultcolumnwidth(String defaultColumnWidth) {
        this.defaultColumnWidth = defaultColumnWidth;
    }
    public String getExpandedrowcount() {
        return expandedRowCount;
    }

    public void setExpandedrowcount(String expandedRowCount) {
        this.expandedRowCount = expandedRowCount;
    }
    public String getExpandedcolumncount() {
        return expandedColumnCount;
    }

    public void setExpandedcolumncount(String expandedColumnCount) {
        this.expandedColumnCount = expandedColumnCount;
    }

    public Worksheet getWorksheet() {
        return worksheet;
    }

    public void setWorksheet(Worksheet worksheet) {
        this.worksheet = worksheet;
    }

}