





import java.util.List;
import java.util.ArrayList;

public class service_architecture_TemplateRepository  {






    private List<ServiceTemplate> servicetemplates;




    private List<GroundTemplate> groundtemplates;


    public service_architecture_TemplateRepository(
    ) {
        this.servicetemplates = new ArrayList<>();
        this.groundtemplates = new ArrayList<>();
    }

    public service_architecture_TemplateRepository(
        ArrayList<ServiceTemplate> servicetemplates,        ArrayList<GroundTemplate> groundtemplates    ) {
        this.servicetemplates = servicetemplates;
        this.groundtemplates = groundtemplates;
    }


    public List<ServiceTemplate> getServicetemplates() {
        return servicetemplates;
    }

    public void addServicetemplate(Servicetemplate servicetemplate) {
        this.servicetemplates.add(servicetemplate);
    }
    public List<GroundTemplate> getGroundtemplates() {
        return groundtemplates;
    }

    public void addGroundtemplate(Groundtemplate groundtemplate) {
        this.groundtemplates.add(groundtemplate);
    }

}