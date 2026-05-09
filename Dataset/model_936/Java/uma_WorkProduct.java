





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement {

    private String report;
    private String estimationConsiderations;
    private String toolMentor;
    private String group2;
    private String template;
    private String estimate;



    public uma_WorkProduct(
        String report,        String estimationConsiderations,        String toolMentor,        String group2,        String template,        String estimate    ) {
        super(
        );
        this.report = report;
        this.estimationConsiderations = estimationConsiderations;
        this.toolMentor = toolMentor;
        this.group2 = group2;
        this.template = template;
        this.estimate = estimate;
    }


    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getEstimationconsiderations() {
        return estimationConsiderations;
    }

    public void setEstimationconsiderations(String estimationConsiderations) {
        this.estimationConsiderations = estimationConsiderations;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
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
    public String getEstimate() {
        return estimate;
    }

    public void setEstimate(String estimate) {
        this.estimate = estimate;
    }


}