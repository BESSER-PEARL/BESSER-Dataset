





import java.util.List;
import java.util.ArrayList;

public class jpql_OrderItem  {

    private String feature;





    private jpql_OrderClause jpql_orderclause;


    public jpql_OrderItem(
        String feature    ) {
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public jpql_OrderClause getJpql_orderclause() {
        return jpql_orderclause;
    }

    public void setJpql_orderclause(jpql_OrderClause jpql_orderclause) {
        this.jpql_orderclause = jpql_orderclause;
    }

}