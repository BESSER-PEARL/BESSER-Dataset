





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLPrintingSetup_Table extends StyledElement {

    private String expandedRowCount;
    private String fullColumns;
    private String defaultColumnWidth;
    private String leftCell;
    private String fullRows;
    private String expandedColumnCount;
    private String topCell;
    private String defaultRowHeight;





    private Worksheet worksheet;


    public SpreadsheetMLPrintingSetup_Table(
        String expandedRowCount,        String fullColumns,        String defaultColumnWidth,        String leftCell,        String fullRows,        String expandedColumnCount,        String topCell,        String defaultRowHeight    ) {
        super(
        );
        this.expandedRowCount = expandedRowCount;
        this.fullColumns = fullColumns;
        this.defaultColumnWidth = defaultColumnWidth;
        this.leftCell = leftCell;
        this.fullRows = fullRows;
        this.expandedColumnCount = expandedColumnCount;
        this.topCell = topCell;
        this.defaultRowHeight = defaultRowHeight;
    }


    public String getExpandedrowcount() {
        return expandedRowCount;
    }

    public void setExpandedrowcount(String expandedRowCount) {
        this.expandedRowCount = expandedRowCount;
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
    public String getLeftcell() {
        return leftCell;
    }

    public void setLeftcell(String leftCell) {
        this.leftCell = leftCell;
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
    public String getDefaultrowheight() {
        return defaultRowHeight;
    }

    public void setDefaultrowheight(String defaultRowHeight) {
        this.defaultRowHeight = defaultRowHeight;
    }

    public Worksheet getWorksheet() {
        return worksheet;
    }

    public void setWorksheet(Worksheet worksheet) {
        this.worksheet = worksheet;
    }

}