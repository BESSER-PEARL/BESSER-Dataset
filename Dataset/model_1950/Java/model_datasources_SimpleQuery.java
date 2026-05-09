





import java.util.List;
import java.util.ArrayList;

public class model_datasources_SimpleQuery extends Query {

    private String countQuery;
    private String query;



    public model_datasources_SimpleQuery(
        String countQuery,        String query    ) {
        super(
        );
        this.countQuery = countQuery;
        this.query = query;
    }


    public String getCountquery() {
        return countQuery;
    }

    public void setCountquery(String countQuery) {
        this.countQuery = countQuery;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}