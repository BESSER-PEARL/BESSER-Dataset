





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private String lastColumn;
    private String sheetList;
    private boolean selectAllSheets;
    private String sheetColumns;
    private String firstColumn;
    private boolean advancedSpearator;
    private String decimalSeparator;
    private String thousandSeparator;
    private String SheetName;



    public connection_FileExcelConnection(
        String lastColumn,        String sheetList,        boolean selectAllSheets,        String sheetColumns,        String firstColumn,        boolean advancedSpearator,        String decimalSeparator,        String thousandSeparator,        String SheetName    ) {
        super(
        );
        this.lastColumn = lastColumn;
        this.sheetList = sheetList;
        this.selectAllSheets = selectAllSheets;
        this.sheetColumns = sheetColumns;
        this.firstColumn = firstColumn;
        this.advancedSpearator = advancedSpearator;
        this.decimalSeparator = decimalSeparator;
        this.thousandSeparator = thousandSeparator;
        this.SheetName = SheetName;
    }


    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
    }
    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
    }
    public boolean getSelectallsheets() {
        return selectAllSheets;
    }

    public void setSelectallsheets(boolean selectAllSheets) {
        this.selectAllSheets = selectAllSheets;
    }
    public String getSheetcolumns() {
        return sheetColumns;
    }

    public void setSheetcolumns(String sheetColumns) {
        this.sheetColumns = sheetColumns;
    }
    public String getFirstcolumn() {
        return firstColumn;
    }

    public void setFirstcolumn(String firstColumn) {
        this.firstColumn = firstColumn;
    }
    public boolean getAdvancedspearator() {
        return advancedSpearator;
    }

    public void setAdvancedspearator(boolean advancedSpearator) {
        this.advancedSpearator = advancedSpearator;
    }
    public String getDecimalseparator() {
        return decimalSeparator;
    }

    public void setDecimalseparator(String decimalSeparator) {
        this.decimalSeparator = decimalSeparator;
    }
    public String getThousandseparator() {
        return thousandSeparator;
    }

    public void setThousandseparator(String thousandSeparator) {
        this.thousandSeparator = thousandSeparator;
    }
    public String getSheetname() {
        return SheetName;
    }

    public void setSheetname(String SheetName) {
        this.SheetName = SheetName;
    }


}