





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private String lastColumn;
    private String decimalSeparator;
    private String SheetName;
    private boolean advancedSpearator;
    private boolean selectAllSheets;
    private String thousandSeparator;
    private String sheetList;
    private String sheetColumns;
    private String firstColumn;



    public connection_FileExcelConnection(
        String lastColumn,        String decimalSeparator,        String SheetName,        boolean advancedSpearator,        boolean selectAllSheets,        String thousandSeparator,        String sheetList,        String sheetColumns,        String firstColumn    ) {
        super(
        );
        this.lastColumn = lastColumn;
        this.decimalSeparator = decimalSeparator;
        this.SheetName = SheetName;
        this.advancedSpearator = advancedSpearator;
        this.selectAllSheets = selectAllSheets;
        this.thousandSeparator = thousandSeparator;
        this.sheetList = sheetList;
        this.sheetColumns = sheetColumns;
        this.firstColumn = firstColumn;
    }


    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
    }
    public String getDecimalseparator() {
        return decimalSeparator;
    }

    public void setDecimalseparator(String decimalSeparator) {
        this.decimalSeparator = decimalSeparator;
    }
    public String getSheetname() {
        return SheetName;
    }

    public void setSheetname(String SheetName) {
        this.SheetName = SheetName;
    }
    public boolean getAdvancedspearator() {
        return advancedSpearator;
    }

    public void setAdvancedspearator(boolean advancedSpearator) {
        this.advancedSpearator = advancedSpearator;
    }
    public boolean getSelectallsheets() {
        return selectAllSheets;
    }

    public void setSelectallsheets(boolean selectAllSheets) {
        this.selectAllSheets = selectAllSheets;
    }
    public String getThousandseparator() {
        return thousandSeparator;
    }

    public void setThousandseparator(String thousandSeparator) {
        this.thousandSeparator = thousandSeparator;
    }
    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
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


}