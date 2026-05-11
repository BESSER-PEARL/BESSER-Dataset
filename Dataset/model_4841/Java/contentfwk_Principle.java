





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Principle extends StrategicElement {

    private String implication;
    private String statementOfPrinciple;
    private String priority;
    private String principleCategory;
    private String metric;
    private String rationale;



    public contentfwk_Principle(
        String implication,        String statementOfPrinciple,        String priority,        String principleCategory,        String metric,        String rationale    ) {
        super(
        );
        this.implication = implication;
        this.statementOfPrinciple = statementOfPrinciple;
        this.priority = priority;
        this.principleCategory = principleCategory;
        this.metric = metric;
        this.rationale = rationale;
    }


    public String getImplication() {
        return implication;
    }

    public void setImplication(String implication) {
        this.implication = implication;
    }
    public String getStatementofprinciple() {
        return statementOfPrinciple;
    }

    public void setStatementofprinciple(String statementOfPrinciple) {
        this.statementOfPrinciple = statementOfPrinciple;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getPrinciplecategory() {
        return principleCategory;
    }

    public void setPrinciplecategory(String principleCategory) {
        this.principleCategory = principleCategory;
    }
    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }


}