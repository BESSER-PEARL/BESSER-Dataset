





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String briefOutline;
    private String representationOptions;



    public uma_ArtifactDescription(
        String briefOutline,        String representationOptions    ) {
        super(
        );
        this.briefOutline = briefOutline;
        this.representationOptions = representationOptions;
    }


    public String getBriefoutline() {
        return briefOutline;
    }

    public void setBriefoutline(String briefOutline) {
        this.briefOutline = briefOutline;
    }
    public String getRepresentationoptions() {
        return representationOptions;
    }

    public void setRepresentationoptions(String representationOptions) {
        this.representationOptions = representationOptions;
    }


}