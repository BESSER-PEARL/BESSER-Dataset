





import java.util.List;
import java.util.ArrayList;

public class testintentionsAssistance_Inst  {






    private testintentionsAssistance_Data testintentionsassistance_data;




    private List<testintentionsAssistance_Variable> testintentionsassistance_variables;


    public testintentionsAssistance_Inst(
    ) {
        this.testintentionsassistance_variables = new ArrayList<>();
    }

    public testintentionsAssistance_Inst(
        ArrayList<testintentionsAssistance_Variable> testintentionsassistance_variables    ) {
        this.testintentionsassistance_variables = testintentionsassistance_variables;
    }


    public testintentionsAssistance_Data getTestintentionsassistance_data() {
        return testintentionsassistance_data;
    }

    public void setTestintentionsassistance_data(testintentionsAssistance_Data testintentionsassistance_data) {
        this.testintentionsassistance_data = testintentionsassistance_data;
    }
    public List<testintentionsAssistance_Variable> getTestintentionsassistance_variables() {
        return testintentionsassistance_variables;
    }

    public void addTestintentionsassistance_variable(Testintentionsassistance_variable testintentionsassistance_variable) {
        this.testintentionsassistance_variables.add(testintentionsassistance_variable);
    }

}