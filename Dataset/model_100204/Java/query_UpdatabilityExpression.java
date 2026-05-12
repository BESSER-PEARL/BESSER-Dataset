





import java.util.List;
import java.util.ArrayList;

public class query_UpdatabilityExpression extends SQLQueryObject {

    private String updatabilityType;





    private query_UpdateOfColumn query_updateofcolumn;




    private List<query_UpdateOfColumn> query_updateofcolumns;


    public query_UpdatabilityExpression(
        String updatabilityType    ) {
        super(
        );
        this.updatabilityType = updatabilityType;
        this.query_updateofcolumns = new ArrayList<>();
    }

    public query_UpdatabilityExpression(
        String updatabilityType        ArrayList<query_UpdateOfColumn> query_updateofcolumns    ) {
        this.updatabilityType = updatabilityType;
        this.query_updateofcolumns = query_updateofcolumns;
    }

    public String getUpdatabilitytype() {
        return updatabilityType;
    }

    public void setUpdatabilitytype(String updatabilityType) {
        this.updatabilityType = updatabilityType;
    }

    public query_UpdateOfColumn getQuery_updateofcolumn() {
        return query_updateofcolumn;
    }

    public void setQuery_updateofcolumn(query_UpdateOfColumn query_updateofcolumn) {
        this.query_updateofcolumn = query_updateofcolumn;
    }
    public List<query_UpdateOfColumn> getQuery_updateofcolumns() {
        return query_updateofcolumns;
    }

    public void addQuery_updateofcolumn(Query_updateofcolumn query_updateofcolumn) {
        this.query_updateofcolumns.add(query_updateofcolumn);
    }

}