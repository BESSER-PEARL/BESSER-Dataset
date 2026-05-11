





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Measure extends Element {






    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Measure contentfwk_measure;




    private contentfwk_Service contentfwk_service;




    private contentfwk_Objective contentfwk_objective;




    private List<contentfwk_Objective> contentfwk_objectives;


    public contentfwk_Measure(
    ) {
        super(
        );
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_objectives = new ArrayList<>();
    }

    public contentfwk_Measure(
        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Objective> contentfwk_objectives    ) {
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_objectives = contentfwk_objectives;
    }


    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Measure getContentfwk_measure() {
        return contentfwk_measure;
    }

    public void setContentfwk_measure(contentfwk_Measure contentfwk_measure) {
        this.contentfwk_measure = contentfwk_measure;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }
    public List<contentfwk_Objective> getContentfwk_objectives() {
        return contentfwk_objectives;
    }

    public void addContentfwk_objective(Contentfwk_objective contentfwk_objective) {
        this.contentfwk_objectives.add(contentfwk_objective);
    }

}