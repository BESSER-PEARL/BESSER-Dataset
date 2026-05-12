





import java.util.List;
import java.util.ArrayList;

public class jPQL_OrderItem  {

    private String feature;





    private jPQL_OrderClause jpql_orderclause;


    public jPQL_OrderItem(
        String feature    ) {
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public jPQL_OrderClause getJpql_orderclause() {
        return jpql_orderclause;
    }

    public void setJpql_orderclause(jPQL_OrderClause jpql_orderclause) {
        this.jpql_orderclause = jpql_orderclause;
    }

}