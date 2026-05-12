





import java.util.List;
import java.util.ArrayList;

public class documentation_TableRow  {

    private String rowCells;





    private documentation_Table documentation_table;


    public documentation_TableRow(
        String rowCells    ) {
        this.rowCells = rowCells;
    }


    public String getRowcells() {
        return rowCells;
    }

    public void setRowcells(String rowCells) {
        this.rowCells = rowCells;
    }

    public documentation_Table getDocumentation_table() {
        return documentation_table;
    }

    public void setDocumentation_table(documentation_Table documentation_table) {
        this.documentation_table = documentation_table;
    }

}