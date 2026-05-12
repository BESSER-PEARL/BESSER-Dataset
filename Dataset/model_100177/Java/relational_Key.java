





import java.util.List;
import java.util.ArrayList;

public class relational_Key  {

    private String name;





    private relational_Table relational_table;




    private List<relational_Column> relational_columns;




    private relational_Table relational_table;


    public relational_Key(
        String name    ) {
        this.name = name;
        this.relational_columns = new ArrayList<>();
    }

    public relational_Key(
        String name        ArrayList<relational_Column> relational_columns    ) {
        this.name = name;
        this.relational_columns = relational_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}