





import java.util.List;
import java.util.ArrayList;

public class pivot_Precedence extends NamedElement {

    private String associativity;
    private int order;





    private pivot_Library pivot_library;


    public pivot_Precedence(
        String associativity,        int order    ) {
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
    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }

    public pivot_Library getPivot_library() {
        return pivot_library;
    }

    public void setPivot_library(pivot_Library pivot_library) {
        this.pivot_library = pivot_library;
    }

}