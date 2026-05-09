





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String representationOptions;
    private String briefOutline;



    public uma_ArtifactDescription(
        String representationOptions,        String briefOutline    ) {
        super(
        );
        this.representationOptions = representationOptions;
        this.briefOutline = briefOutline;
    }


    public String getRepresentationoptions() {
        return representationOptions;
    }

    public void setRepresentationoptions(String representationOptions) {
        this.representationOptions = representationOptions;
    }
    public String getBriefoutline() {
        return briefOutline;
    }

    public void setBriefoutline(String briefOutline) {
        this.briefOutline = briefOutline;
    }


}