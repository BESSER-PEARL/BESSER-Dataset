





import java.util.List;
import java.util.ArrayList;

public class spreadsheet_Sheet  {

    private String SheetName;
    private int SheetIndex;



    public spreadsheet_Sheet(
        String SheetName,        int SheetIndex    ) {
        this.SheetName = SheetName;
        this.SheetIndex = SheetIndex;
    }


    public String getSheetname() {
        return SheetName;
    }

    public void setSheetname(String SheetName) {
        this.SheetName = SheetName;
    }
    public int getSheetindex() {
        return SheetIndex;
    }

    public void setSheetindex(int SheetIndex) {
        this.SheetIndex = SheetIndex;
    }


}