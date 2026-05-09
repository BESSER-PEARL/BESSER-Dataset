





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_QueryCondition extends DdsReadCondition {

    private String query;
    private String queryParameters;



    public ddsMetamodel_QueryCondition(
        String query,        String queryParameters    ) {
        super(
        );
        this.query = query;
        this.queryParameters = queryParameters;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getQueryparameters() {
        return queryParameters;
    }

    public void setQueryparameters(String queryParameters) {
        this.queryParameters = queryParameters;
    }


}