





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_Worksheet  {

    private String name;





    private Workbook workbook;




    private Table table;


    public SpreadsheetMLSimplified_Worksheet(
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
    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}