





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProduct extends ContentElement {






    private uma_WorkProductType uma_workproducttype;




    private uma_WorkProductDescriptor uma_workproductdescriptor;




    private List<uma_ToolMentor> uma_toolmentors;




    private List<uma_Report> uma_reports;




    private List<uma_EstimationConsiderations> uma_estimationconsiderationss;




    private uma_Task uma_task;




    private uma_Role uma_role;




    private uma_Role uma_role;




    private uma_Domain uma_domain;




    private uma_Task uma_task;




    private uma_State uma_state;




    private uma_Task uma_task;




    private List<uma_Template> uma_templates;


    public uma_WorkProduct(
    ) {
        super(
        );
        this.uma_toolmentors = new ArrayList<>();
        this.uma_reports = new ArrayList<>();
        this.uma_estimationconsiderationss = new ArrayList<>();
        this.uma_templates = new ArrayList<>();
    }

    public uma_WorkProduct(
        ArrayList<uma_ToolMentor> uma_toolmentors,        ArrayList<uma_Report> uma_reports,        ArrayList<uma_EstimationConsiderations> uma_estimationconsiderationss,        ArrayList<uma_Template> uma_templates    ) {
        this.uma_toolmentors = uma_toolmentors;
        this.uma_reports = uma_reports;
        this.uma_estimationconsiderationss = uma_estimationconsiderationss;
        this.uma_templates = uma_templates;
    }


    public uma_WorkProductType getUma_workproducttype() {
        return uma_workproducttype;
    }

    public void setUma_workproducttype(uma_WorkProductType uma_workproducttype) {
        this.uma_workproducttype = uma_workproducttype;
    }
    public uma_WorkProductDescriptor getUma_workproductdescriptor() {
        return uma_workproductdescriptor;
    }

    public void setUma_workproductdescriptor(uma_WorkProductDescriptor uma_workproductdescriptor) {
        this.uma_workproductdescriptor = uma_workproductdescriptor;
    }
    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }
    public List<uma_Report> getUma_reports() {
        return uma_reports;
    }

    public void addUma_report(Uma_report uma_report) {
        this.uma_reports.add(uma_report);
    }
    public List<uma_EstimationConsiderations> getUma_estimationconsiderationss() {
        return uma_estimationconsiderationss;
    }

    public void addUma_estimationconsiderations(Uma_estimationconsiderations uma_estimationconsiderations) {
        this.uma_estimationconsiderationss.add(uma_estimationconsiderations);
    }
    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }
    public uma_Role getUma_role() {
        return uma_role;
    }

    public void setUma_role(uma_Role uma_role) {
        this.uma_role = uma_role;
    }
    public uma_Role getUma_role() {
        return uma_role;
    }

    public void setUma_role(uma_Role uma_role) {
        this.uma_role = uma_role;
    }
    public uma_Domain getUma_domain() {
        return uma_domain;
    }

    public void setUma_domain(uma_Domain uma_domain) {
        this.uma_domain = uma_domain;
    }
    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }
    public uma_State getUma_state() {
        return uma_state;
    }

    public void setUma_state(uma_State uma_state) {
        this.uma_state = uma_state;
    }
    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }
    public List<uma_Template> getUma_templates() {
        return uma_templates;
    }

    public void addUma_template(Uma_template uma_template) {
        this.uma_templates.add(uma_template);
    }

}