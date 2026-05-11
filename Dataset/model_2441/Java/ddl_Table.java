





import java.util.List;
import java.util.ArrayList;

public class ddl_Table extends DataElement {






    private List<ddl_Column> ddl_columns;




    private ddl_Schema ddl_schema;


    public ddl_Table(
    ) {
        super(
        );
        this.ddl_columns = new ArrayList<>();
    }

    public ddl_Table(
        ArrayList<ddl_Column> ddl_columns    ) {
        this.ddl_columns = ddl_columns;
    }


    public List<ddl_Column> getDdl_columns() {
        return ddl_columns;
    }

    public void addDdl_column(Ddl_column ddl_column) {
        this.ddl_columns.add(ddl_column);
    }
    public ddl_Schema getDdl_schema() {
        return ddl_schema;
    }

    public void setDdl_schema(ddl_Schema ddl_schema) {
        this.ddl_schema = ddl_schema;
    }

}