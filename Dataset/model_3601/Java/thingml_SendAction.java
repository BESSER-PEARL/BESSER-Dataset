





import java.util.List;
import java.util.ArrayList;

public class thingml_SendAction extends Action {






    private thingml_Message thingml_message;




    private thingml_Port thingml_port;




    private List<thingml_Expression> thingml_expressions;


    public thingml_SendAction(
    ) {
        super(
        );
        this.thingml_expressions = new ArrayList<>();
    }

    public thingml_SendAction(
        ArrayList<thingml_Expression> thingml_expressions    ) {
        this.thingml_expressions = thingml_expressions;
    }


    public thingml_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingml_Message thingml_message) {
        this.thingml_message = thingml_message;
    }
    public thingml_Port getThingml_port() {
        return thingml_port;
    }

    public void setThingml_port(thingml_Port thingml_port) {
        this.thingml_port = thingml_port;
    }
    public List<thingml_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}