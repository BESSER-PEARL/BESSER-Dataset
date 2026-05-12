





import java.util.List;
import java.util.ArrayList;

public class relational_ForeignKey  {






    private List<relational_Column> relational_columns;




    private relational_Key relational_key;




    private relational_Table relational_table;




    private relational_Key relational_key;




    private relational_Table relational_table;


    public relational_ForeignKey(
    ) {
        this.relational_columns = new ArrayList<>();
    }

    public relational_ForeignKey(
        ArrayList<relational_Column> relational_columns    ) {
        this.relational_columns = relational_columns;
    }


    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_Key getRelational_key() {
        return relational_key;
    }

    public void setRelational_key(relational_Key relational_key) {
        this.relational_key = relational_key;
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public relational_Key getRelational_key() {
        return relational_key;
    }

    public void setRelational_key(relational_Key relational_key) {
        this.relational_key = relational_key;
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}