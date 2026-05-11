





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Principle extends StrategicElement {

    private String statementOfPrinciple;
    private String implication;
    private String rationale;
    private String priority;
    private String metric;
    private String principleCategory;



    public contentfwk_Principle(
        String statementOfPrinciple,        String implication,        String rationale,        String priority,        String metric,        String principleCategory    ) {
        super(
        );
        this.statementOfPrinciple = statementOfPrinciple;
        this.implication = implication;
        this.rationale = rationale;
        this.priority = priority;
        this.metric = metric;
        this.principleCategory = principleCategory;
    }


    public String getStatementofprinciple() {
        return statementOfPrinciple;
    }

    public void setStatementofprinciple(String statementOfPrinciple) {
        this.statementOfPrinciple = statementOfPrinciple;
    }
    public String getImplication() {
        return implication;
    }

    public void setImplication(String implication) {
        this.implication = implication;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }
    public String getPrinciplecategory() {
        return principleCategory;
    }

    public void setPrinciplecategory(String principleCategory) {
        this.principleCategory = principleCategory;
    }


}