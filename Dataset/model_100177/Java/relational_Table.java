





import java.util.List;
import java.util.ArrayList;

public class relational_Table  {

    private String name;





    private List<relational_Column> relational_columns;


    public relational_Table(
        String name    ) {
        this.name = name;
        this.relational_columns = new ArrayList<>();
    }

    public relational_Table(
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

    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }

}