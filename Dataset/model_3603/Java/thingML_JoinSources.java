





import java.util.List;
import java.util.ArrayList;

public class thingML_JoinSources extends Source, ReferencedElmt {

    private String name;





    private thingML_Message thingml_message;




    private List<thingML_Expression> thingml_expressions;


    public thingML_JoinSources(
        String name    ) {
        super(
        );
        this.name = name;
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_JoinSources(
        String name        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.name = name;
        this.thingml_expressions = thingml_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public thingML_Message getThingml_message() {
        return thingml_message;
    }

    public void setThingml_message(thingML_Message thingml_message) {
        this.thingml_message = thingml_message;
    }
    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}