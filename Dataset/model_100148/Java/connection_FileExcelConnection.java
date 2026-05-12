





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private boolean selectAllSheets;
    private String firstColumn;
    private String sheetColumns;
    private String sheetList;
    private String thousandSeparator;
    private String SheetName;
    private String lastColumn;
    private boolean advancedSpearator;
    private String decimalSeparator;



    public connection_FileExcelConnection(
        boolean selectAllSheets,        String firstColumn,        String sheetColumns,        String sheetList,        String thousandSeparator,        String SheetName,        String lastColumn,        boolean advancedSpearator,        String decimalSeparator    ) {
        super(
        );
        this.selectAllSheets = selectAllSheets;
        this.firstColumn = firstColumn;
        this.sheetColumns = sheetColumns;
        this.sheetList = sheetList;
        this.thousandSeparator = thousandSeparator;
        this.SheetName = SheetName;
        this.lastColumn = lastColumn;
        this.advancedSpearator = advancedSpearator;
        this.decimalSeparator = decimalSeparator;
    }


    public boolean getSelectallsheets() {
        return selectAllSheets;
    }

    public void setSelectallsheets(boolean selectAllSheets) {
        this.selectAllSheets = selectAllSheets;
    }
    public String getFirstcolumn() {
        return firstColumn;
    }

    public void setFirstcolumn(String firstColumn) {
        this.firstColumn = firstColumn;
    }
    public String getSheetcolumns() {
        return sheetColumns;
    }

    public void setSheetcolumns(String sheetColumns) {
        this.sheetColumns = sheetColumns;
    }
    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
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
    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
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


}