





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Boot  {






    private List<mancoosimm_Service> mancoosimm_services;


    public mancoosimm_Boot(
    ) {
        this.mancoosimm_services = new ArrayList<>();
    }

    public mancoosimm_Boot(
        ArrayList<mancoosimm_Service> mancoosimm_services    ) {
        this.mancoosimm_services = mancoosimm_services;
    }


    public List<mancoosimm_Service> getMancoosimm_services() {
        return mancoosimm_services;
    }

    public void addMancoosimm_service(Mancoosimm_service mancoosimm_service) {
        this.mancoosimm_services.add(mancoosimm_service);
    }

}