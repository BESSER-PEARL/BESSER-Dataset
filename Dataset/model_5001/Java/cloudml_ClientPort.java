





import java.util.List;
import java.util.ArrayList;

public class cloudml_ClientPort extends ArtefactPort {

    private boolean isOptional;





    private cloudml_Artefact cloudml_artefact;




    private cloudml_Binding cloudml_binding;


    public cloudml_ClientPort(
        boolean isOptional    ) {
        super(
        );
        this.isOptional = isOptional;
    }


    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }

    public cloudml_Artefact getCloudml_artefact() {
        return cloudml_artefact;
    }

    public void setCloudml_artefact(cloudml_Artefact cloudml_artefact) {
        this.cloudml_artefact = cloudml_artefact;
    }
    public cloudml_Binding getCloudml_binding() {
        return cloudml_binding;
    }

    public void setCloudml_binding(cloudml_Binding cloudml_binding) {
        this.cloudml_binding = cloudml_binding;
    }

}