





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_Table extends StyledElement {

    private String defaultRowHeight;
    private String fullColumns;
    private String fullRows;
    private String defaultColumnWidth;
    private String leftCell;
    private String expandedRowCount;
    private String topCell;
    private String expandedColumnCount;





    private Worksheet worksheet;


    public SpreadsheetMLBasicDef_Table(
        String defaultRowHeight,        String fullColumns,        String fullRows,        String defaultColumnWidth,        String leftCell,        String expandedRowCount,        String topCell,        String expandedColumnCount    ) {
        super(
        );
        this.defaultRowHeight = defaultRowHeight;
        this.fullColumns = fullColumns;
        this.fullRows = fullRows;
        this.defaultColumnWidth = defaultColumnWidth;
        this.leftCell = leftCell;
        this.expandedRowCount = expandedRowCount;
        this.topCell = topCell;
        this.expandedColumnCount = expandedColumnCount;
    }


    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
    }
    public String getFullcolumns() {
        return fullColumns;
    }

    public void setFullcolumns(String fullColumns) {
        this.fullColumns = fullColumns;
    }
    public String getFullrows() {
        return fullRows;
    }

    public void setFullrows(String fullRows) {
        this.fullRows = fullRows;
    }
    public String getDefaultcolumnwidth() {
        return defaultColumnWidth;
    }

    public void setDefaultcolumnwidth(String defaultColumnWidth) {
        this.defaultColumnWidth = defaultColumnWidth;
    }
    public String getLeftcell() {
        return leftCell;
    }

    public void setLeftcell(String leftCell) {
        this.leftCell = leftCell;
    }
    public String getExpandedrowcount() {
        return expandedRowCount;
    }

    public void setExpandedrowcount(String expandedRowCount) {
        this.expandedRowCount = expandedRowCount;
    }
    public String getTopcell() {
        return topCell;
    }

    public void setTopcell(String topCell) {
        this.topCell = topCell;
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