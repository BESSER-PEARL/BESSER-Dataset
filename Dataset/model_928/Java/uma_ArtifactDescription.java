





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String notation;
    private String representation;
    private String briefOutline;
    private String representationOptions;



    public uma_ArtifactDescription(
        String notation,        String representation,        String briefOutline,        String representationOptions    ) {
        super(
        );
        this.notation = notation;
        this.representation = representation;
        this.briefOutline = briefOutline;
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