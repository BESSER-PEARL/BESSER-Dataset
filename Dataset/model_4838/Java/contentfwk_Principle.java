





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Principle extends StrategicElement {

    private String priority;
    private String statementOfPrinciple;
    private String rationale;
    private String principleCategory;
    private String implication;
    private String metric;



    public contentfwk_Principle(
        String priority,        String statementOfPrinciple,        String rationale,        String principleCategory,        String implication,        String metric    ) {
        super(
        );
        this.priority = priority;
        this.statementOfPrinciple = statementOfPrinciple;
        this.rationale = rationale;
        this.principleCategory = principleCategory;
        this.implication = implication;
        this.metric = metric;
    }


    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getStatementofprinciple() {
        return statementOfPrinciple;
    }

    public void setStatementofprinciple(String statementOfPrinciple) {
        this.statementOfPrinciple = statementOfPrinciple;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getPrinciplecategory() {
        return principleCategory;
    }

    public void setPrinciplecategory(String principleCategory) {
        this.principleCategory = principleCategory;
    }
    public String getImplication() {
        return implication;
    }

    public void setImplication(String implication) {
        this.implication = implication;
    }
    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }


}