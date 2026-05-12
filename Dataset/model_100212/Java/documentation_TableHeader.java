





import java.util.List;
import java.util.ArrayList;

public class documentation_TableHeader  {

    private String headerCells;





    private documentation_Table documentation_table;


    public documentation_TableHeader(
        String headerCells    ) {
        this.headerCells = headerCells;
    }


    public String getHeadercells() {
        return headerCells;
    }

    public void setHeadercells(String headerCells) {
        this.headerCells = headerCells;
    }

    public documentation_Table getDocumentation_table() {
        return documentation_table;
    }

    public void setDocumentation_table(documentation_Table documentation_table) {
        this.documentation_table = documentation_table;
    }

}