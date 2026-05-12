





import java.util.List;
import java.util.ArrayList;

public class mql_AliasAttributeExpression extends SelectExpression, Variable {

    private String attributes;





    private mql_UpdateItem mql_updateitem;


    public mql_AliasAttributeExpression(
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

    public mql_UpdateItem getMql_updateitem() {
        return mql_updateitem;
    }

    public void setMql_updateitem(mql_UpdateItem mql_updateitem) {
        this.mql_updateitem = mql_updateitem;
    }

}