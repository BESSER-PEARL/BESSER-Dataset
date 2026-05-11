





import java.util.List;
import java.util.ArrayList;

public class diva_Context extends NamedElement {

    private String verdict;





    private List<diva_VariableValue> diva_variablevalues;




    private List<diva_Priority> diva_prioritys;




    private diva_Scenario diva_scenario;


    public diva_Context(
        String verdict    ) {
        super(
        );
        this.verdict = verdict;
        this.diva_variablevalues = new ArrayList<>();
        this.diva_prioritys = new ArrayList<>();
    }

    public diva_Context(
        String verdict        ArrayList<diva_VariableValue> diva_variablevalues,        ArrayList<diva_Priority> diva_prioritys    ) {
        this.verdict = verdict;
        this.diva_variablevalues = diva_variablevalues;
        this.diva_prioritys = diva_prioritys;
    }

    public String getVerdict() {
        return verdict;
    }

    public void setVerdict(String verdict) {
        this.verdict = verdict;
    }

    public List<diva_VariableValue> getDiva_variablevalues() {
        return diva_variablevalues;
    }

    public void addDiva_variablevalue(Diva_variablevalue diva_variablevalue) {
        this.diva_variablevalues.add(diva_variablevalue);
    }
    public List<diva_Priority> getDiva_prioritys() {
        return diva_prioritys;
    }

    public void addDiva_priority(Diva_priority diva_priority) {
        this.diva_prioritys.add(diva_priority);
    }
    public diva_Scenario getDiva_scenario() {
        return diva_scenario;
    }

    public void setDiva_scenario(diva_Scenario diva_scenario) {
        this.diva_scenario = diva_scenario;
    }

}