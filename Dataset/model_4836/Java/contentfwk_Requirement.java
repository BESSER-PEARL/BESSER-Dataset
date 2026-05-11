





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Requirement extends StrategicElement {

    private String statementOfRequirement;
    private String acceptanceCriteria;
    private String rationale;



    public contentfwk_Requirement(
        String statementOfRequirement,        String acceptanceCriteria,        String rationale    ) {
        super(
        );
        this.statementOfRequirement = statementOfRequirement;
        this.acceptanceCriteria = acceptanceCriteria;
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
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }


}