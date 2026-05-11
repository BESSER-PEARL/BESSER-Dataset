





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Requirement extends StrategicElement {

    private String acceptanceCriteria;
    private String statementOfRequirement;
    private String rationale;



    public contentfwk_Requirement(
        String acceptanceCriteria,        String statementOfRequirement,        String rationale    ) {
        super(
        );
        this.acceptanceCriteria = acceptanceCriteria;
        this.statementOfRequirement = statementOfRequirement;
        this.rationale = rationale;
    }


    public String getAcceptancecriteria() {
        return acceptanceCriteria;
    }

    public void setAcceptancecriteria(String acceptanceCriteria) {
        this.acceptanceCriteria = acceptanceCriteria;
    }
    public String getStatementofrequirement() {
        return statementOfRequirement;
    }

    public void setStatementofrequirement(String statementOfRequirement) {
        this.statementOfRequirement = statementOfRequirement;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }


}