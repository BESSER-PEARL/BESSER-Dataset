





import java.util.List;
import java.util.ArrayList;

public class model_ServiceInstance extends Service, ElementWithResources {

    private String totalData;
    private String id;
    private String address;
    private String containers;
    private String totalMessages;





    private model_StringToServiceInstance model_stringtoserviceinstance;




    private model_Host model_host;


    public model_ServiceInstance(
        String totalData,        String id,        String address,        String containers,        String totalMessages    ) {
        super(
        );
        this.totalData = totalData;
        this.id = id;
        this.address = address;
        this.containers = containers;
        this.totalMessages = totalMessages;
    }


    public String getTotaldata() {
        return totalData;
    }

    public void setTotaldata(String totalData) {
        this.totalData = totalData;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getContainers() {
        return containers;
    }

    public void setContainers(String containers) {
        this.containers = containers;
    }
    public String getTotalmessages() {
        return totalMessages;
    }

    public void setTotalmessages(String totalMessages) {
        this.totalMessages = totalMessages;
    }

    public model_StringToServiceInstance getModel_stringtoserviceinstance() {
        return model_stringtoserviceinstance;
    }

    public void setModel_stringtoserviceinstance(model_StringToServiceInstance model_stringtoserviceinstance) {
        this.model_stringtoserviceinstance = model_stringtoserviceinstance;
    }
    public model_Host getModel_host() {
        return model_host;
    }

    public void setModel_host(model_Host model_host) {
        this.model_host = model_host;
    }

}