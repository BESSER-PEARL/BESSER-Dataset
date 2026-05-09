





import java.util.List;
import java.util.ArrayList;

public class dom_ArrayLiteral extends Expression {






    private List<dom_IArrayElement> dom_iarrayelements;


    public dom_ArrayLiteral(
    ) {
        super(
        );
        this.dom_iarrayelements = new ArrayList<>();
    }

    public dom_ArrayLiteral(
        ArrayList<dom_IArrayElement> dom_iarrayelements    ) {
        this.dom_iarrayelements = dom_iarrayelements;
    }


    public List<dom_IArrayElement> getDom_iarrayelements() {
        return dom_iarrayelements;
    }

    public void addDom_iarrayelement(Dom_iarrayelement dom_iarrayelement) {
        this.dom_iarrayelements.add(dom_iarrayelement);
    }

}