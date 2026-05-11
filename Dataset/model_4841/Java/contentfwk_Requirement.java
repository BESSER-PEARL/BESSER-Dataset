





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Requirement extends StrategicElement {

    private String rationale;
    private String statementOfRequirement;
    private String acceptanceCriteria;



    public contentfwk_Requirement(
        String rationale,        String statementOfRequirement,        String acceptanceCriteria    ) {
        super(
        );
        this.rationale = rationale;
        this.statementOfRequirement = statementOfRequirement;
        this.acceptanceCriteria = acceptanceCriteria;
    }


    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getStatementofrequirement() {
        return statementOfRequirement;
    }

    public void setStatementofrequirement(String statementOfRequirement) {
        this.statementOfRequirement = statementOfRequirement;
    }
    public String getAcceptancecriteria() {
        return acceptanceCriteria;
    }

    public void setAcceptancecriteria(String acceptanceCriteria) {
        this.acceptanceCriteria = acceptanceCriteria;
    }


}