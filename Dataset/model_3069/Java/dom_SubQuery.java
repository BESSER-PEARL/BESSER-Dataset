





import java.util.List;
import java.util.ArrayList;

public class dom_SubQuery extends Expression {






    private List<dom_SelectStatement> dom_selectstatements;


    public dom_SubQuery(
    ) {
        super(
        );
        this.dom_selectstatements = new ArrayList<>();
    }

    public dom_SubQuery(
        ArrayList<dom_SelectStatement> dom_selectstatements    ) {
        this.dom_selectstatements = dom_selectstatements;
    }


    public List<dom_SelectStatement> getDom_selectstatements() {
        return dom_selectstatements;
    }

    public void addDom_selectstatement(Dom_selectstatement dom_selectstatement) {
        this.dom_selectstatements.add(dom_selectstatement);
    }

}