





import java.util.List;
import java.util.ArrayList;

public class cloudml_ArtefactInstance extends WithProperties {






    private cloudml_NodeInstance cloudml_nodeinstance;




    private List<cloudml_ClientPortInstance> cloudml_clientportinstances;




    private List<cloudml_ServerPortInstance> cloudml_serverportinstances;




    private cloudml_Composite cloudml_composite;


    public cloudml_ArtefactInstance(
    ) {
        super(
        );
        this.cloudml_clientportinstances = new ArrayList<>();
        this.cloudml_serverportinstances = new ArrayList<>();
    }

    public cloudml_ArtefactInstance(
        ArrayList<cloudml_ClientPortInstance> cloudml_clientportinstances,        ArrayList<cloudml_ServerPortInstance> cloudml_serverportinstances    ) {
        this.cloudml_clientportinstances = cloudml_clientportinstances;
        this.cloudml_serverportinstances = cloudml_serverportinstances;
    }


    public cloudml_NodeInstance getCloudml_nodeinstance() {
        return cloudml_nodeinstance;
    }

    public void setCloudml_nodeinstance(cloudml_NodeInstance cloudml_nodeinstance) {
        this.cloudml_nodeinstance = cloudml_nodeinstance;
    }
    public List<cloudml_ClientPortInstance> getCloudml_clientportinstances() {
        return cloudml_clientportinstances;
    }

    public void addCloudml_clientportinstance(Cloudml_clientportinstance cloudml_clientportinstance) {
        this.cloudml_clientportinstances.add(cloudml_clientportinstance);
    }
    public List<cloudml_ServerPortInstance> getCloudml_serverportinstances() {
        return cloudml_serverportinstances;
    }

    public void addCloudml_serverportinstance(Cloudml_serverportinstance cloudml_serverportinstance) {
        this.cloudml_serverportinstances.add(cloudml_serverportinstance);
    }
    public cloudml_Composite getCloudml_composite() {
        return cloudml_composite;
    }

    public void setCloudml_composite(cloudml_Composite cloudml_composite) {
        this.cloudml_composite = cloudml_composite;
    }

}