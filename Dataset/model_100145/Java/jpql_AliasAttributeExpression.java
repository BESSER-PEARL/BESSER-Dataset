





import java.util.List;
import java.util.ArrayList;

public class jpql_AliasAttributeExpression extends SelectExpression, Variable {

    private String attributes;





    private jpql_UpdateItem jpql_updateitem;


    public jpql_AliasAttributeExpression(
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

    public jpql_UpdateItem getJpql_updateitem() {
        return jpql_updateitem;
    }

    public void setJpql_updateitem(jpql_UpdateItem jpql_updateitem) {
        this.jpql_updateitem = jpql_updateitem;
    }

}