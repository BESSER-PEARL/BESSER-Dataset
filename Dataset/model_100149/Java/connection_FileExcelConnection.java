





import java.util.List;
import java.util.ArrayList;

public class connection_FileExcelConnection extends FileConnection {

    private boolean advancedSpearator;
    private String decimalSeparator;
    private String sheetList;
    private String firstColumn;
    private String generationMode;
    private boolean selectAllSheets;
    private String SheetName;
    private String thousandSeparator;
    private String lastColumn;
    private String sheetColumns;



    public connection_FileExcelConnection(
        boolean advancedSpearator,        String decimalSeparator,        String sheetList,        String firstColumn,        String generationMode,        boolean selectAllSheets,        String SheetName,        String thousandSeparator,        String lastColumn,        String sheetColumns    ) {
        super(
        );
        this.advancedSpearator = advancedSpearator;
        this.decimalSeparator = decimalSeparator;
        this.sheetList = sheetList;
        this.firstColumn = firstColumn;
        this.generationMode = generationMode;
        this.selectAllSheets = selectAllSheets;
        this.SheetName = SheetName;
        this.thousandSeparator = thousandSeparator;
        this.lastColumn = lastColumn;
        this.sheetColumns = sheetColumns;
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
    public String getSheetlist() {
        return sheetList;
    }

    public void setSheetlist(String sheetList) {
        this.sheetList = sheetList;
    }
    public String getFirstcolumn() {
        return firstColumn;
    }

    public void setFirstcolumn(String firstColumn) {
        this.firstColumn = firstColumn;
    }
    public String getGenerationmode() {
        return generationMode;
    }

    public void setGenerationmode(String generationMode) {
        this.generationMode = generationMode;
    }
    public boolean getSelectallsheets() {
        return selectAllSheets;
    }

    public void setSelectallsheets(boolean selectAllSheets) {
        this.selectAllSheets = selectAllSheets;
    }
    public String getSheetname() {
        return SheetName;
    }

    public void setSheetname(String SheetName) {
        this.SheetName = SheetName;
    }
    public String getThousandseparator() {
        return thousandSeparator;
    }

    public void setThousandseparator(String thousandSeparator) {
        this.thousandSeparator = thousandSeparator;
    }
    public String getLastcolumn() {
        return lastColumn;
    }

    public void setLastcolumn(String lastColumn) {
        this.lastColumn = lastColumn;
    }
    public String getSheetcolumns() {
        return sheetColumns;
    }

    public void setSheetcolumns(String sheetColumns) {
        this.sheetColumns = sheetColumns;
    }


}