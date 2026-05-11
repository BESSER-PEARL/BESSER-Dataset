





import java.util.List;
import java.util.ArrayList;

public class dom_CollectionExpression extends LiteralExpression {






    private dom_Type dom_type;




    private dom_CollectionInitValue dom_collectioninitvalue;


    public dom_CollectionExpression(
    ) {
        super(
        );
    }



    public dom_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(dom_Type dom_type) {
        this.dom_type = dom_type;
    }
    public dom_CollectionInitValue getDom_collectioninitvalue() {
        return dom_collectioninitvalue;
    }

    public void setDom_collectioninitvalue(dom_CollectionInitValue dom_collectioninitvalue) {
        this.dom_collectioninitvalue = dom_collectioninitvalue;
    }

}