





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Table extends rdb_Relation, rdb_DbObject {






    private Schema schema;


    public mm_rdb_Table(
    ) {
        super(
        );
    }



    public Schema getSchema() {
        return schema;
    }

    public void setSchema(Schema schema) {
        this.schema = schema;
    }

}