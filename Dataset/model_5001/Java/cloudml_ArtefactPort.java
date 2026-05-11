





import java.util.List;
import java.util.ArrayList;

public class cloudml_ArtefactPort extends WithProperties {

    private boolean isRemote;
    private int portNumber;





    private cloudml_Artefact cloudml_artefact;




    private cloudml_ArtefactPortInstance cloudml_artefactportinstance;


    public cloudml_ArtefactPort(
        boolean isRemote,        int portNumber    ) {
        super(
        );
        this.isRemote = isRemote;
        this.portNumber = portNumber;
    }


    public boolean getIsremote() {
        return isRemote;
    }

    public void setIsremote(boolean isRemote) {
        this.isRemote = isRemote;
    }
    public int getPortnumber() {
        return portNumber;
    }

    public void setPortnumber(int portNumber) {
        this.portNumber = portNumber;
    }

    public cloudml_Artefact getCloudml_artefact() {
        return cloudml_artefact;
    }

    public void setCloudml_artefact(cloudml_Artefact cloudml_artefact) {
        this.cloudml_artefact = cloudml_artefact;
    }
    public cloudml_ArtefactPortInstance getCloudml_artefactportinstance() {
        return cloudml_artefactportinstance;
    }

    public void setCloudml_artefactportinstance(cloudml_ArtefactPortInstance cloudml_artefactportinstance) {
        this.cloudml_artefactportinstance = cloudml_artefactportinstance;
    }

}