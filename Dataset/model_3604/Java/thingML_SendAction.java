





import java.util.List;
import java.util.ArrayList;

public class thingML_SendAction extends Action {






    private List<thingML_Expression> thingml_expressions;




    private thingML_Message thingml_message;




    private thingML_Port thingml_port;


    public thingML_SendAction(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_SendAction(
        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }
    public thingML_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingML_Message thingml_message) {
        this.thingml_message = thingml_message;
    }
    public thingML_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingML_Port thingml_port) {
        this.thingml_port = thingml_port;
    }

}