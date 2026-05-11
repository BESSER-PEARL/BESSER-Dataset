





import java.util.List;
import java.util.ArrayList;

public class service_template_GroundTemplate  {

    private String name;





    private List<BoundProcessModel> boundprocessmodels;




    private List<BoundTemplateParameter> boundtemplateparameters;




    private template_service_Service template_service_service;


    public service_template_GroundTemplate(
        String name    ) {
        this.name = name;
        this.boundprocessmodels = new ArrayList<>();
        this.boundtemplateparameters = new ArrayList<>();
    }

    public service_template_GroundTemplate(
        String name        ArrayList<BoundProcessModel> boundprocessmodels,        ArrayList<BoundTemplateParameter> boundtemplateparameters    ) {
        this.name = name;
        this.boundprocessmodels = boundprocessmodels;
        this.boundtemplateparameters = boundtemplateparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<BoundProcessModel> getBoundprocessmodels() {
        return boundprocessmodels;
    }

    public void addBoundprocessmodel(Boundprocessmodel boundprocessmodel) {
        this.boundprocessmodels.add(boundprocessmodel);
    }
    public List<BoundTemplateParameter> getBoundtemplateparameters() {
        return boundtemplateparameters;
    }

    public void addBoundtemplateparameter(Boundtemplateparameter boundtemplateparameter) {
        this.boundtemplateparameters.add(boundtemplateparameter);
    }
    public template_service_Service getTemplate_service_service() {
        return template_service_service;
    }

    public void setTemplate_service_service(template_service_Service template_service_service) {
        this.template_service_service = template_service_service;
    }

}