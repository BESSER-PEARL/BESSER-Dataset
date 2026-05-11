





import java.util.List;
import java.util.ArrayList;

public class cloudml_ExternalComponentInstance extends ComponentInstance {

    private String ips;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_VMPortInstance> cloudml_vmportinstances;


    public cloudml_ExternalComponentInstance(
        String ips    ) {
        super(
        );
        this.ips = ips;
        this.cloudml_vmportinstances = new ArrayList<>();
    }

    public cloudml_ExternalComponentInstance(
        String ips        ArrayList<cloudml_VMPortInstance> cloudml_vmportinstances    ) {
        this.ips = ips;
        this.cloudml_vmportinstances = cloudml_vmportinstances;
    }

    public String getIps() {
        return ips;
    }

    public void setIps(String ips) {
        this.ips = ips;
    }

    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }
    public List<cloudml_VMPortInstance> getCloudml_vmportinstances() {
        return cloudml_vmportinstances;
    }

    public void addCloudml_vmportinstance(Cloudml_vmportinstance cloudml_vmportinstance) {
        this.cloudml_vmportinstances.add(cloudml_vmportinstance);
    }

}