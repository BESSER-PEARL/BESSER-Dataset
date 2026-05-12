





import java.util.List;
import java.util.ArrayList;

public class newP_UnaryOperator extends Term {

    private String name;





    private newP_Term newp_term;


    public newP_UnaryOperator(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public newP_Term getNewp_term() {
        return newp_term;
    }

    public void setNewp_term(newP_Term newp_term) {
        this.newp_term = newp_term;
    }

}