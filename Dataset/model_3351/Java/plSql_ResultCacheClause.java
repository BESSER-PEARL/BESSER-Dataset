





import java.util.List;
import java.util.ArrayList;

public class plSql_ResultCacheClause extends FunctionClause {

    private String dataSources;



    public plSql_ResultCacheClause(
        String dataSources    ) {
        super(
        );
        this.dataSources = dataSources;
    }


    public String getDatasources() {
        return dataSources;
    }

    public void setDatasources(String dataSources) {
        this.dataSources = dataSources;
    }


}