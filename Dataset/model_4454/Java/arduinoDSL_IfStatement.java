





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_IfStatement extends SimpleStatement {






    private arduinoDSL_SimpleStatement arduinodsl_simplestatement;




    private arduinoDSL_BooleanExpression arduinodsl_booleanexpression;




    private arduinoDSL_SimpleStatement arduinodsl_simplestatement;




    private List<arduinoDSL_SimpleStatement> arduinodsl_simplestatements;


    public arduinoDSL_IfStatement(
    ) {
        super(
        );
        this.arduinodsl_simplestatements = new ArrayList<>();
    }

    public arduinoDSL_IfStatement(
        ArrayList<arduinoDSL_SimpleStatement> arduinodsl_simplestatements    ) {
        this.arduinodsl_simplestatements = arduinodsl_simplestatements;
    }


    public arduinoDSL_SimpleStatement getArduinodsl_simplestatement() {
        return arduinodsl_simplestatement;
    }

    public void setArduinodsl_simplestatement(arduinoDSL_SimpleStatement arduinodsl_simplestatement) {
        this.arduinodsl_simplestatement = arduinodsl_simplestatement;
    }
    public arduinoDSL_BooleanExpression getArduinodsl_booleanexpression() {
        return arduinodsl_booleanexpression;
    }

    public void setArduinodsl_booleanexpression(arduinoDSL_BooleanExpression arduinodsl_booleanexpression) {
        this.arduinodsl_booleanexpression = arduinodsl_booleanexpression;
    }
    public arduinoDSL_SimpleStatement getArduinodsl_simplestatement() {
        return arduinodsl_simplestatement;
    }

    public void setArduinodsl_simplestatement(arduinoDSL_SimpleStatement arduinodsl_simplestatement) {
        this.arduinodsl_simplestatement = arduinodsl_simplestatement;
    }
    public List<arduinoDSL_SimpleStatement> getArduinodsl_simplestatements() {
        return arduinodsl_simplestatements;
    }

    public void addArduinodsl_simplestatement(Arduinodsl_simplestatement arduinodsl_simplestatement) {
        this.arduinodsl_simplestatements.add(arduinodsl_simplestatement);
    }

}