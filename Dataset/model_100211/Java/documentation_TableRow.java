





import java.util.List;
import java.util.ArrayList;

public class documentation_TableRow  {






    private documentation_Table documentation_table;




    private List<documentation_TableCell> documentation_tablecells;


    public documentation_TableRow(
    ) {
        this.documentation_tablecells = new ArrayList<>();
    }

    public documentation_TableRow(
        ArrayList<documentation_TableCell> documentation_tablecells    ) {
        this.documentation_tablecells = documentation_tablecells;
    }


    public documentation_Table getDocumentation_table() {
        return documentation_table;
    }

    public void setDocumentation_table(documentation_Table documentation_table) {
        this.documentation_table = documentation_table;
    }
    public List<documentation_TableCell> getDocumentation_tablecells() {
        return documentation_tablecells;
    }

    public void addDocumentation_tablecell(Documentation_tablecell documentation_tablecell) {
        this.documentation_tablecells.add(documentation_tablecell);
    }

}