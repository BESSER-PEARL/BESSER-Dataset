





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private boolean selectAllSheets;
    private String sheetColumns;
    private String sheetList;
    private boolean advancedSpearator;
    private String thousandSeparator;
    private String SheetName;
    private String firstColumn;
    private String decimalSeparator;
    private String lastColumn;



    public connection_FileExcelConnection(
        boolean selectAllSheets,        String sheetColumns,        String sheetList,        boolean advancedSpearator,        String thousandSeparator,        String SheetName,        String firstColumn,        String decimalSeparator,        String lastColumn    ) {
        super(
        );
        this.selectAllSheets = selectAllSheets;
        this.sheetColumns = sheetColumns;
        this.sheetList = sheetList;
        this.advancedSpearator = advancedSpearator;
        this.thousandSeparator = thousandSeparator;
        this.SheetName = SheetName;
        this.firstColumn = firstColumn;
        this.decimalSeparator = decimalSeparator;
        this.lastColumn = lastColumn;
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
    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
    }
    public boolean getAdvancedspearator() {
        return advancedSpearator;
    }

    public void setAdvancedspearator(boolean advancedSpearator) {
        this.advancedSpearator = advancedSpearator;
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
    public String getFirstcolumn() {
        return firstColumn;
    }

    public void setFirstcolumn(String firstColumn) {
        this.firstColumn = firstColumn;
    }
    public String getDecimalseparator() {
        return decimalSeparator;
    }

    public void setDecimalseparator(String decimalSeparator) {
        this.decimalSeparator = decimalSeparator;
    }
    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
    }


}