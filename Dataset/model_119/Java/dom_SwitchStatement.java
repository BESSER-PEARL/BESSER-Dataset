





import java.util.List;
import java.util.ArrayList;

public class dom_SwitchStatement extends Statement {






    private List<dom_SwitchElement> dom_switchelements;




    private dom_Expression dom_expression;


    public dom_SwitchStatement(
    ) {
        super(
        );
        this.dom_switchelements = new ArrayList<>();
    }

    public dom_SwitchStatement(
        ArrayList<dom_SwitchElement> dom_switchelements    ) {
        this.dom_switchelements = dom_switchelements;
    }


    public List<dom_SwitchElement> getDom_switchelements() {
        return dom_switchelements;
    }

    public void addDom_switchelement(Dom_switchelement dom_switchelement) {
        this.dom_switchelements.add(dom_switchelement);
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}