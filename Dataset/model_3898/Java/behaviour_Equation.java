





import java.util.List;
import java.util.ArrayList;

public class behaviour_Equation  {






    private List<behaviour_Expression> behaviour_expressions;




    private behaviour_AttributeClass behaviour_attributeclass;




    private behaviour_EquationBehaviour behaviour_equationbehaviour;


    public behaviour_Equation(
    ) {
        this.behaviour_expressions = new ArrayList<>();
    }

    public behaviour_Equation(
        ArrayList<behaviour_Expression> behaviour_expressions    ) {
        this.behaviour_expressions = behaviour_expressions;
    }


    public List<behaviour_Expression> getBehaviour_expressions() {
        return behaviour_expressions;
    }

    public void addBehaviour_expression(Behaviour_expression behaviour_expression) {
        this.behaviour_expressions.add(behaviour_expression);
    }
    public behaviour_AttributeClass getBehaviour_attributeclass() {
        return behaviour_attributeclass;
    }

    public void setBehaviour_attributeclass(behaviour_AttributeClass behaviour_attributeclass) {
        this.behaviour_attributeclass = behaviour_attributeclass;
    }
    public behaviour_EquationBehaviour getBehaviour_equationbehaviour() {
        return behaviour_equationbehaviour;
    }

    public void setBehaviour_equationbehaviour(behaviour_EquationBehaviour behaviour_equationbehaviour) {
        this.behaviour_equationbehaviour = behaviour_equationbehaviour;
    }

}