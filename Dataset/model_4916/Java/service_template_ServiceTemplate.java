





import java.util.List;
import java.util.ArrayList;

public class service_template_ServiceTemplate  {

    private String URI;





    private List<ServiceParameter> serviceparameters;


    public service_template_ServiceTemplate(
        String URI    ) {
        this.URI = URI;
        this.serviceparameters = new ArrayList<>();
    }

    public service_template_ServiceTemplate(
        String URI        ArrayList<ServiceParameter> serviceparameters    ) {
        this.URI = URI;
        this.serviceparameters = serviceparameters;
    }

    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public List<ServiceParameter> getServiceparameters() {
        return serviceparameters;
    }

    public void addServiceparameter(Serviceparameter serviceparameter) {
        this.serviceparameters.add(serviceparameter);
    }

}