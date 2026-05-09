





import java.util.List;
import java.util.ArrayList;

public class pivot_Precedence extends NamedElement {

    private String order;
    private String associativity;



    public pivot_Precedence(
        String order,        String associativity    ) {
        super(
        );
        this.order = order;
        this.associativity = associativity;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getAssociativity() {
        return associativity;
    }

    public void setAssociativity(String associativity) {
        this.associativity = associativity;
    }


}