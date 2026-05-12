





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private String decimalSeparator;
    private String SheetName;
    private String sheetColumns;
    private String firstColumn;
    private String thousandSeparator;
    private boolean advancedSpearator;
    private String sheetList;
    private boolean selectAllSheets;
    private String lastColumn;



    public connection_FileExcelConnection(
        String decimalSeparator,        String SheetName,        String sheetColumns,        String firstColumn,        String thousandSeparator,        boolean advancedSpearator,        String sheetList,        boolean selectAllSheets,        String lastColumn    ) {
        super(
        );
        this.decimalSeparator = decimalSeparator;
        this.SheetName = SheetName;
        this.sheetColumns = sheetColumns;
        this.firstColumn = firstColumn;
        this.thousandSeparator = thousandSeparator;
        this.advancedSpearator = advancedSpearator;
        this.sheetList = sheetList;
        this.selectAllSheets = selectAllSheets;
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
    public String getThousandseparator() {
        return thousandSeparator;
    }

    public void setThousandseparator(String thousandSeparator) {
        this.thousandSeparator = thousandSeparator;
    }
    public boolean getAdvancedspearator() {
        return advancedSpearator;
    }

    public void setAdvancedspearator(boolean advancedSpearator) {
        this.advancedSpearator = advancedSpearator;
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
    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
    }


}