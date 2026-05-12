





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorksheetOpt_Worksheet  {

    private String protected;
    private String name;
    private String rightToLeft;





    private Workbook workbook;




    private Table table;




    private WorksheetOptionsElt worksheetoptionselt;


    public SpreadsheetMLWorksheetOpt_Worksheet(
        String protected,        String name,        String rightToLeft    ) {
        this.protected = protected;
        this.name = name;
        this.rightToLeft = rightToLeft;
    }


    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRighttoleft() {
        return rightToLeft;
    }

    public void setRighttoleft(String rightToLeft) {
        this.rightToLeft = rightToLeft;
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
    public WorksheetOptionsElt getWorksheetoptionselt() {
        return worksheetoptionselt;
    }

    public void setWorksheetoptionselt(WorksheetOptionsElt worksheetoptionselt) {
        this.worksheetoptionselt = worksheetoptionselt;
    }

}