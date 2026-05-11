





import java.util.List;
import java.util.ArrayList;

public class altarica_Assignment extends Instruction {






    private altarica_Expression altarica_expression;




    private altarica_NameRef altarica_nameref;


    public altarica_Assignment(
    ) {
        super(
        );
    }



    public altarica_Expression getAltarica_expression() {
        return altarica_expression;
    }

    public void setAltarica_expression(altarica_Expression altarica_expression) {
        this.altarica_expression = altarica_expression;
    }
    public altarica_NameRef getAltarica_nameref() {
        return altarica_nameref;
    }

    public void setAltarica_nameref(altarica_NameRef altarica_nameref) {
        this.altarica_nameref = altarica_nameref;
    }

}