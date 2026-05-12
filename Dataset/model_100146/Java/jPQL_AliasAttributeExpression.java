





import java.util.List;
import java.util.ArrayList;

public class jPQL_AliasAttributeExpression extends Variable, OrderBySpec {

    private String direction;
    private String attributes;





    private jPQL_UpdateItem jpql_updateitem;




    private jPQL_GroupByClause jpql_groupbyclause;


    public jPQL_AliasAttributeExpression(
        String direction,        String attributes    ) {
        super(
        );
        this.direction = direction;
        this.attributes = attributes;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }

    public jPQL_UpdateItem getJpql_updateitem() {
        return jpql_updateitem;
    }

    public void setJpql_updateitem(jPQL_UpdateItem jpql_updateitem) {
        this.jpql_updateitem = jpql_updateitem;
    }
    public jPQL_GroupByClause getJpql_groupbyclause() {
        return jpql_groupbyclause;
    }

    public void setJpql_groupbyclause(jPQL_GroupByClause jpql_groupbyclause) {
        this.jpql_groupbyclause = jpql_groupbyclause;
    }

}