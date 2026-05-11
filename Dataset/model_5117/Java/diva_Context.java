





import java.util.List;
import java.util.ArrayList;

public class diva_Context extends NamedElement {

    private String verdict;





    private diva_Scenario diva_scenario;


    public diva_Context(
        String verdict    ) {
        super(
        );
        this.verdict = verdict;
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

}