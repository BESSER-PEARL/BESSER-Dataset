





import java.util.List;
import java.util.ArrayList;

public class cloudml_VMInstance extends ExternalComponentInstance {

    private String publicAddress;
    private String id;





    private cloudml_Cloud cloudml_cloud;




    private List<cloudml_VMPortInstance> cloudml_vmportinstances;




    private cloudml_CloudMLModel cloudml_cloudmlmodel;


    public cloudml_VMInstance(
        String publicAddress,        String id    ) {
        super(
        );
        this.publicAddress = publicAddress;
        this.id = id;
        this.cloudml_vmportinstances = new ArrayList<>();
    }

    public cloudml_VMInstance(
        String publicAddress,        String id        ArrayList<cloudml_VMPortInstance> cloudml_vmportinstances    ) {
        this.publicAddress = publicAddress;
        this.id = id;
        this.cloudml_vmportinstances = cloudml_vmportinstances;
    }

    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public cloudml_Cloud getCloudml_cloud() {
        return cloudml_cloud;
    }

    public void setCloudml_cloud(cloudml_Cloud cloudml_cloud) {
        this.cloudml_cloud = cloudml_cloud;
    }
    public List<cloudml_VMPortInstance> getCloudml_vmportinstances() {
        return cloudml_vmportinstances;
    }

    public void addCloudml_vmportinstance(Cloudml_vmportinstance cloudml_vmportinstance) {
        this.cloudml_vmportinstances.add(cloudml_vmportinstance);
    }
    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }

}