





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement {

    private String template;
    private String toolMentor;
    private String report;
    private String estimate;
    private String estimationConsiderations;
    private String group2;



    public uma_WorkProduct(
        String template,        String toolMentor,        String report,        String estimate,        String estimationConsiderations,        String group2    ) {
        super(
        );
        this.template = template;
        this.toolMentor = toolMentor;
        this.report = report;
        this.estimate = estimate;
        this.estimationConsiderations = estimationConsiderations;
        this.group2 = group2;
    }


    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}