





import java.util.List;
import java.util.ArrayList;

public class gremlin_IndexCall extends MethodCall {

    private String indexName;
    private String indexQuery;
    private String indexProperty;



    public gremlin_IndexCall(
        String indexName,        String indexQuery,        String indexProperty    ) {
        super(
        );
        this.indexName = indexName;
        this.indexQuery = indexQuery;
        this.indexProperty = indexProperty;
    }


    public String getIndexname() {
        return indexName;
    }

    public void setIndexname(String indexName) {
        this.indexName = indexName;
    }
    public String getIndexquery() {
        return indexQuery;
    }

    public void setIndexquery(String indexQuery) {
        this.indexQuery = indexQuery;
    }
    public String getIndexproperty() {
        return indexProperty;
    }

    public void setIndexproperty(String indexProperty) {
        this.indexProperty = indexProperty;
    }


}