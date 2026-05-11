





import java.util.List;
import java.util.ArrayList;

public class arduinoDSL_ElseStatement extends SimpleStatement {






    private List<arduinoDSL_SimpleStatement> arduinodsl_simplestatements;


    public arduinoDSL_ElseStatement(
    ) {
        super(
        );
        this.arduinodsl_simplestatements = new ArrayList<>();
    }

    public arduinoDSL_ElseStatement(
        ArrayList<arduinoDSL_SimpleStatement> arduinodsl_simplestatements    ) {
        this.arduinodsl_simplestatements = arduinodsl_simplestatements;
    }


    public List<arduinoDSL_SimpleStatement> getArduinodsl_simplestatements() {
        return arduinodsl_simplestatements;
    }

    public void addArduinodsl_simplestatement(Arduinodsl_simplestatement arduinodsl_simplestatement) {
        this.arduinodsl_simplestatements.add(arduinodsl_simplestatement);
    }

}