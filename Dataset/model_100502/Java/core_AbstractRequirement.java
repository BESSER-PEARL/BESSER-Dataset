





import java.util.List;
import java.util.ArrayList;

public class core_AbstractRequirement extends VerifiableElement {

    private String risk;





    private core_Variable core_variable;




    private core_VerificationActivity core_verificationactivity;




    private List<core_VerificationActivity> core_verificationactivitys;




    private List<core_Variable> core_variables;




    private core_AbstractRequirement core_abstractrequirement;


    public core_AbstractRequirement(
        String risk    ) {
        super(
        );
        this.risk = risk;
        this.core_verificationactivitys = new ArrayList<>();
        this.core_variables = new ArrayList<>();
    }

    public core_AbstractRequirement(
        String risk        ArrayList<core_VerificationActivity> core_verificationactivitys,        ArrayList<core_Variable> core_variables    ) {
        this.risk = risk;
        this.core_verificationactivitys = core_verificationactivitys;
        this.core_variables = core_variables;
    }

    public String getRisk() {
        return risk;
    }

    public void setRisk(String risk) {
        this.risk = risk;
    }

    public core_Variable getCore_variable() {
        return core_variable;
    }

    public void setCore_variable(core_Variable core_variable) {
        this.core_variable = core_variable;
    }
    public core_VerificationActivity getCore_verificationactivity() {
        return core_verificationactivity;
    }

    public void setCore_verificationactivity(core_VerificationActivity core_verificationactivity) {
        this.core_verificationactivity = core_verificationactivity;
    }
    public List<core_VerificationActivity> getCore_verificationactivitys() {
        return core_verificationactivitys;
    }

    public void addCore_verificationactivity(Core_verificationactivity core_verificationactivity) {
        this.core_verificationactivitys.add(core_verificationactivity);
    }
    public List<core_Variable> getCore_variables() {
        return core_variables;
    }

    public void addCore_variable(Core_variable core_variable) {
        this.core_variables.add(core_variable);
    }
    public core_AbstractRequirement getCore_abstractrequirement() {
        return core_abstractrequirement;
    }

    public void setCore_abstractrequirement(core_AbstractRequirement core_abstractrequirement) {
        this.core_abstractrequirement = core_abstractrequirement;
    }

}