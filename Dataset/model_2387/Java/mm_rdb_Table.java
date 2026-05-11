





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Table  {

    private String name;





    private List<Column> columns;




    private Schema schema;


    public mm_rdb_Table(
        String name    ) {
        this.name = name;
        this.columns = new ArrayList<>();
    }

    public mm_rdb_Table(
        String name        ArrayList<Column> columns    ) {
        this.name = name;
        this.columns = columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }
    public Schema getSchema() {
        return schema;
    }

    public void setSchema(Schema schema) {
        this.schema = schema;
    }

}