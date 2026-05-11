





import java.util.List;
import java.util.ArrayList;

public class testintentionsAssistance_Function extends AbstractElement {

    private String methode;





    private List<testintentionsAssistance_OutVariable> testintentionsassistance_outvariables;




    private testintentionsAssistance_Variable testintentionsassistance_variable;




    private List<testintentionsAssistance_Variable> testintentionsassistance_variables;


    public testintentionsAssistance_Function(
        String methode    ) {
        super(
        );
        this.methode = methode;
        this.testintentionsassistance_outvariables = new ArrayList<>();
        this.testintentionsassistance_variables = new ArrayList<>();
    }

    public testintentionsAssistance_Function(
        String methode        ArrayList<testintentionsAssistance_OutVariable> testintentionsassistance_outvariables,        ArrayList<testintentionsAssistance_Variable> testintentionsassistance_variables    ) {
        this.methode = methode;
        this.testintentionsassistance_outvariables = testintentionsassistance_outvariables;
        this.testintentionsassistance_variables = testintentionsassistance_variables;
    }

    public String getMethode() {
        return methode;
    }

    public void setMethode(String methode) {
        this.methode = methode;
    }

    public List<testintentionsAssistance_OutVariable> getTestintentionsassistance_outvariables() {
        return testintentionsassistance_outvariables;
    }

    public void addTestintentionsassistance_outvariable(Testintentionsassistance_outvariable testintentionsassistance_outvariable) {
        this.testintentionsassistance_outvariables.add(testintentionsassistance_outvariable);
    }
    public testintentionsAssistance_Variable getTestintentionsassistance_variable() {
        return testintentionsassistance_variable;
    }

    public void setTestintentionsassistance_variable(testintentionsAssistance_Variable testintentionsassistance_variable) {
        this.testintentionsassistance_variable = testintentionsassistance_variable;
    }
    public List<testintentionsAssistance_Variable> getTestintentionsassistance_variables() {
        return testintentionsassistance_variables;
    }

    public void addTestintentionsassistance_variable(Testintentionsassistance_variable testintentionsassistance_variable) {
        this.testintentionsassistance_variables.add(testintentionsassistance_variable);
    }

}