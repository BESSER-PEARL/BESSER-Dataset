





import java.util.List;
import java.util.ArrayList;

public class thingML_PrintAction extends Action {

    private boolean line;





    private List<thingML_Expression> thingml_expressions;


    public thingML_PrintAction(
        boolean line    ) {
        super(
        );
        this.line = line;
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_PrintAction(
        boolean line        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.line = line;
        this.thingml_expressions = thingml_expressions;
    }

    public boolean getLine() {
        return line;
    }

    public void setLine(boolean line) {
        this.line = line;
    }

    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}