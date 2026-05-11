





import java.util.List;
import java.util.ArrayList;

public class model_table_TableConstraint  {

    private String name;





    private Table table;


    public model_table_TableConstraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}