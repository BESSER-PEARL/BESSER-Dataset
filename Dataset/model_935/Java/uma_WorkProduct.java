





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement {

    private String estimate;
    private String toolMentor;
    private String estimationConsiderations;
    private String report;
    private String group2;
    private String template;



    public uma_WorkProduct(
        String estimate,        String toolMentor,        String estimationConsiderations,        String report,        String group2,        String template    ) {
        super(
        );
        this.estimate = estimate;
        this.toolMentor = toolMentor;
        this.estimationConsiderations = estimationConsiderations;
        this.report = report;
        this.group2 = group2;
        this.template = template;
    }


    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }


}