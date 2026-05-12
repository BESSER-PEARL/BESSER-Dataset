





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_Worksheet  {

    private String name;





    private Workbook workbook;


    public SpreadsheetMLWorkbookProp_Worksheet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Workbook getWorkbook() {
        return workbook;
    }

    public void setWorkbook(Workbook workbook) {
        this.workbook = workbook;
    }

}