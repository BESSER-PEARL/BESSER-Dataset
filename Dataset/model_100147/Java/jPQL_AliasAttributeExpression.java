





import java.util.List;
import java.util.ArrayList;

public class jPQL_AliasAttributeExpression extends Variable, SelectExpression {

    private String attributes;





    private jPQL_UpdateItem jpql_updateitem;


    public jPQL_AliasAttributeExpression(
        String attributes    ) {
        super(
        );
        this.attributes = attributes;
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

}