





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Principle extends StrategicElement {

    private String statementOfPrinciple;
    private String rationale;
    private String metric;
    private String principleCategory;
    private String implication;
    private String priority;



    public contentfwk_Principle(
        String statementOfPrinciple,        String rationale,        String metric,        String principleCategory,        String implication,        String priority    ) {
        super(
        );
        this.statementOfPrinciple = statementOfPrinciple;
        this.rationale = rationale;
        this.metric = metric;
        this.principleCategory = principleCategory;
        this.implication = implication;
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
    public String getImplication() {
        return implication;
    }

    public void setImplication(String implication) {
        this.implication = implication;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }


}