





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String briefOutline;
    private String representationOptions;
    private String notation;
    private String representation;



    public uma_ArtifactDescription(
        String briefOutline,        String representationOptions,        String notation,        String representation    ) {
        super(
        );
        this.briefOutline = briefOutline;
        this.representationOptions = representationOptions;
        this.notation = notation;
        this.representation = representation;
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
    public String getNotation() {
        return notation;
    }

    public void setNotation(String notation) {
        this.notation = notation;
    }
    public String getRepresentation() {
        return representation;
    }

    public void setRepresentation(String representation) {
        this.representation = representation;
    }


}