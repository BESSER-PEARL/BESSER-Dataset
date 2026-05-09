





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement, FulfillableElement {






    private List<uma_Template> uma_templates;




    private List<uma_Report> uma_reports;




    private List<uma_ToolMentor> uma_toolmentors;




    private uma_Deliverable uma_deliverable;




    private List<uma_EstimationConsiderations> uma_estimationconsiderationss;


    public uma_WorkProduct(
    ) {
        super(
        );
        this.uma_templates = new ArrayList<>();
        this.uma_reports = new ArrayList<>();
        this.uma_toolmentors = new ArrayList<>();
        this.uma_estimationconsiderationss = new ArrayList<>();
    }

    public uma_WorkProduct(
        ArrayList<uma_Template> uma_templates,        ArrayList<uma_Report> uma_reports,        ArrayList<uma_ToolMentor> uma_toolmentors,        ArrayList<uma_EstimationConsiderations> uma_estimationconsiderationss    ) {
        this.uma_templates = uma_templates;
        this.uma_reports = uma_reports;
        this.uma_toolmentors = uma_toolmentors;
        this.uma_estimationconsiderationss = uma_estimationconsiderationss;
    }


    public List<uma_Template> getUma_templates() {
        return uma_templates;
    }

    public void addUma_template(Uma_template uma_template) {
        this.uma_templates.add(uma_template);
    }
    public List<uma_Report> getUma_reports() {
        return uma_reports;
    }

    public void addUma_report(Uma_report uma_report) {
        this.uma_reports.add(uma_report);
    }
    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }
    public uma_Deliverable getUma_deliverable() {
        return uma_deliverable;
    }

    public void setUma_deliverable(uma_Deliverable uma_deliverable) {
        this.uma_deliverable = uma_deliverable;
    }
    public List<uma_EstimationConsiderations> getUma_estimationconsiderationss() {
        return uma_estimationconsiderationss;
    }

    public void addUma_estimationconsiderations(Uma_estimationconsiderations uma_estimationconsiderations) {
        this.uma_estimationconsiderationss.add(uma_estimationconsiderations);
    }

}