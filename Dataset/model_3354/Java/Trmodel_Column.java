





import java.util.List;
import java.util.ArrayList;

public class Trmodel_Column  {

    private String tableName;
    private String Name;





    private Trmodel_Operation trmodel_operation;


    public Trmodel_Column(
        String tableName,        String Name    ) {
        this.tableName = tableName;
        this.Name = Name;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Trmodel_Operation getTrmodel_operation() {
        return trmodel_operation;
    }

    public void setTrmodel_operation(Trmodel_Operation trmodel_operation) {
        this.trmodel_operation = trmodel_operation;
    }

}