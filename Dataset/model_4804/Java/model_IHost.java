





import java.util.List;
import java.util.ArrayList;

public class model_IHost  {

    private String address;
    private String name;





    private model_INetwork model_inetwork;




    private List<model_IServiceInfo> model_iserviceinfos;


    public model_IHost(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
        this.model_iserviceinfos = new ArrayList<>();
    }

    public model_IHost(
        String address,        String name        ArrayList<model_IServiceInfo> model_iserviceinfos    ) {
        this.address = address;
        this.name = name;
        this.model_iserviceinfos = model_iserviceinfos;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_INetwork getModel_inetwork() {
        return model_inetwork;
    }

    public void setModel_inetwork(model_INetwork model_inetwork) {
        this.model_inetwork = model_inetwork;
    }
    public List<model_IServiceInfo> getModel_iserviceinfos() {
        return model_iserviceinfos;
    }

    public void addModel_iserviceinfo(Model_iserviceinfo model_iserviceinfo) {
        this.model_iserviceinfos.add(model_iserviceinfo);
    }

}