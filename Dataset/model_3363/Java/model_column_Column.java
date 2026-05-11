





import java.util.List;
import java.util.ArrayList;

public class model_column_Column extends NameProvider {

    private String type;





    private Table table;


    public model_column_Column(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}