





import java.util.List;
import java.util.ArrayList;

public class securityTest_WebComponent  {

    private String path;





    private List<securityTest_WebComponent> securitytest_webcomponents;




    private securityTest_TargetOfEvaluation securitytest_targetofevaluation;




    private List<securityTest_Input> securitytest_inputs;


    public securityTest_WebComponent(
        String path    ) {
        this.path = path;
        this.securitytest_webcomponents = new ArrayList<>();
        this.securitytest_inputs = new ArrayList<>();
    }

    public securityTest_WebComponent(
        String path        ArrayList<securityTest_WebComponent> securitytest_webcomponents,        ArrayList<securityTest_Input> securitytest_inputs    ) {
        this.path = path;
        this.securitytest_webcomponents = securitytest_webcomponents;
        this.securitytest_inputs = securitytest_inputs;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public List<securityTest_WebComponent> getSecuritytest_webcomponents() {
        return securitytest_webcomponents;
    }

    public void addSecuritytest_webcomponent(Securitytest_webcomponent securitytest_webcomponent) {
        this.securitytest_webcomponents.add(securitytest_webcomponent);
    }
    public securityTest_TargetOfEvaluation getSecuritytest_targetofevaluation() {
        return securitytest_targetofevaluation;
    }

    public void setSecuritytest_targetofevaluation(securityTest_TargetOfEvaluation securitytest_targetofevaluation) {
        this.securitytest_targetofevaluation = securitytest_targetofevaluation;
    }
    public List<securityTest_Input> getSecuritytest_inputs() {
        return securitytest_inputs;
    }

    public void addSecuritytest_input(Securitytest_input securitytest_input) {
        this.securitytest_inputs.add(securitytest_input);
    }

}