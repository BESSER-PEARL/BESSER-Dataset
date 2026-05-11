





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Principle extends StrategicElement {

    private String principleCategory;
    private String metric;
    private String priority;
    private String statementOfPrinciple;
    private String implication;
    private String rationale;



    public contentfwk_Principle(
        String principleCategory,        String metric,        String priority,        String statementOfPrinciple,        String implication,        String rationale    ) {
        super(
        );
        this.principleCategory = principleCategory;
        this.metric = metric;
        this.priority = priority;
        this.statementOfPrinciple = statementOfPrinciple;
        this.implication = implication;
        this.rationale = rationale;
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


}