





import java.util.List;
import java.util.ArrayList;

public class dom_MapExpression extends LiteralExpression {






    private List<dom_KeyValue> dom_keyvalues;


    public dom_MapExpression(
    ) {
        super(
        );
        this.dom_keyvalues = new ArrayList<>();
    }

    public dom_MapExpression(
        ArrayList<dom_KeyValue> dom_keyvalues    ) {
        this.dom_keyvalues = dom_keyvalues;
    }


    public List<dom_KeyValue> getDom_keyvalues() {
        return dom_keyvalues;
    }

    public void addDom_keyvalue(Dom_keyvalue dom_keyvalue) {
        this.dom_keyvalues.add(dom_keyvalue);
    }

}