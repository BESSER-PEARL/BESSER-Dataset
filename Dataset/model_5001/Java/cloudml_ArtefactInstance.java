





import java.util.List;
import java.util.ArrayList;

public class cloudml_ArtefactInstance extends WithProperties {






    private cloudml_Artefact cloudml_artefact;




    private cloudml_NodeInstance cloudml_nodeinstance;




    private cloudml_Composite cloudml_composite;


    public cloudml_ArtefactInstance(
    ) {
        super(
        );
    }



    public cloudml_Artefact getCloudml_artefact() {
        return cloudml_artefact;
    }

    public void setCloudml_artefact(cloudml_Artefact cloudml_artefact) {
        this.cloudml_artefact = cloudml_artefact;
    }
    public cloudml_NodeInstance getCloudml_nodeinstance() {
        return cloudml_nodeinstance;
    }

    public void setCloudml_nodeinstance(cloudml_NodeInstance cloudml_nodeinstance) {
        this.cloudml_nodeinstance = cloudml_nodeinstance;
    }
    public cloudml_Composite getCloudml_composite() {
        return cloudml_composite;
    }

    public void setCloudml_composite(cloudml_Composite cloudml_composite) {
        this.cloudml_composite = cloudml_composite;
    }

}