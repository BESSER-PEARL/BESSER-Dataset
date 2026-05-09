





import java.util.List;
import java.util.ArrayList;

public class pivot_Precedence extends NamedElement {

    private String associativity;
    private String order;





    private pivot_Operation pivot_operation;


    public pivot_Precedence(
        String associativity,        String order    ) {
        super(
        );
        this.associativity = associativity;
        this.order = order;
    }


    public String getAssociativity() {
        return associativity;
    }

    public void setAssociativity(String associativity) {
        this.associativity = associativity;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }

    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}