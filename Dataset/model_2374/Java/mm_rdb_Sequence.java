





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Sequence extends DbObject {

    private int cacheSize;





    private Schema schema;


    public mm_rdb_Sequence(
        int cacheSize    ) {
        super(
        );
        this.cacheSize = cacheSize;
    }


    public int getCachesize() {
        return cacheSize;
    }

    public void setCachesize(int cacheSize) {
        this.cacheSize = cacheSize;
    }

    public Schema getSchema() {
        return schema;
    }

    public void setSchema(Schema schema) {
        this.schema = schema;
    }

}