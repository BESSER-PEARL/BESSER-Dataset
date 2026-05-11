





import java.util.List;
import java.util.ArrayList;

public class diva_Context extends NamedElement {

    private String verdict;





    private diva_Scenario diva_scenario;




    private List<diva_Priority> diva_prioritys;




    private List<diva_VariableValue> diva_variablevalues;


    public diva_Context(
        String verdict    ) {
        super(
        );
        this.verdict = verdict;
        this.diva_prioritys = new ArrayList<>();
        this.diva_variablevalues = new ArrayList<>();
    }

    public diva_Context(
        String verdict        ArrayList<diva_Priority> diva_prioritys,        ArrayList<diva_VariableValue> diva_variablevalues    ) {
        this.verdict = verdict;
        this.diva_prioritys = diva_prioritys;
        this.diva_variablevalues = diva_variablevalues;
    }

    public String getVerdict() {
        return verdict;
    }

    public void setVerdict(String verdict) {
        this.verdict = verdict;
    }

    public diva_Scenario getDiva_scenario() {
        return diva_scenario;
    }

    public void setDiva_scenario(diva_Scenario diva_scenario) {
        this.diva_scenario = diva_scenario;
    }
    public List<diva_Priority> getDiva_prioritys() {
        return diva_prioritys;
    }

    public void addDiva_priority(Diva_priority diva_priority) {
        this.diva_prioritys.add(diva_priority);
    }
    public List<diva_VariableValue> getDiva_variablevalues() {
        return diva_variablevalues;
    }

    public void addDiva_variablevalue(Diva_variablevalue diva_variablevalue) {
        this.diva_variablevalues.add(diva_variablevalue);
    }

}