





import java.util.List;
import java.util.ArrayList;

public class cloudml_VMInstance extends ExternalComponentInstance {

    private String id;
    private String publicAddress;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private cloudml_Cloud cloudml_cloud;




    private List<cloudml_VMPortInstance> cloudml_vmportinstances;


    public cloudml_VMInstance(
        String id,        String publicAddress    ) {
        super(
        );
        this.id = id;
        this.publicAddress = publicAddress;
        this.cloudml_vmportinstances = new ArrayList<>();
    }

    public cloudml_VMInstance(
        String id,        String publicAddress        ArrayList<cloudml_VMPortInstance> cloudml_vmportinstances    ) {
        this.id = id;
        this.publicAddress = publicAddress;
        this.cloudml_vmportinstances = cloudml_vmportinstances;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPublicaddress() {
        return publicAddress;
    }

    public void setPublicaddress(String publicAddress) {
        this.publicAddress = publicAddress;
    }

    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
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

}