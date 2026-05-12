





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private String sheetList;
    private String SheetName;
    private boolean selectAllSheets;
    private String lastColumn;
    private String firstColumn;
    private boolean advancedSpearator;
    private String thousandSeparator;
    private String decimalSeparator;
    private String sheetColumns;



    public connection_FileExcelConnection(
        String sheetList,        String SheetName,        boolean selectAllSheets,        String lastColumn,        String firstColumn,        boolean advancedSpearator,        String thousandSeparator,        String decimalSeparator,        String sheetColumns    ) {
        super(
        );
        this.sheetList = sheetList;
        this.SheetName = SheetName;
        this.selectAllSheets = selectAllSheets;
        this.lastColumn = lastColumn;
        this.firstColumn = firstColumn;
        this.advancedSpearator = advancedSpearator;
        this.thousandSeparator = thousandSeparator;
        this.decimalSeparator = decimalSeparator;
        this.sheetColumns = sheetColumns;
    }


    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
    }
    public String getSheetname() {
        return SheetName;
    }

    public void setSheetname(String SheetName) {
        this.SheetName = SheetName;
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
    public String getThousandseparator() {
        return thousandSeparator;
    }

    public void setThousandseparator(String thousandSeparator) {
        this.thousandSeparator = thousandSeparator;
    }
    public String getDecimalseparator() {
        return decimalSeparator;
    }

    public void setDecimalseparator(String decimalSeparator) {
        this.decimalSeparator = decimalSeparator;
    }
    public String getSheetcolumns() {
        return sheetColumns;
    }

    public void setSheetcolumns(String sheetColumns) {
        this.sheetColumns = sheetColumns;
    }


}