





import java.util.List;
import java.util.ArrayList;

public class thingML_ArrayInit extends Expression {






    private List<thingML_Expression> thingml_expressions;


    public thingML_ArrayInit(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_ArrayInit(
        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}