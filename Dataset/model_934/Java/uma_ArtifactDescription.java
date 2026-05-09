





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String representation;
    private String briefOutline;
    private String notation;
    private String representationOptions;



    public uma_ArtifactDescription(
        String representation,        String briefOutline,        String notation,        String representationOptions    ) {
        super(
        );
        this.representation = representation;
        this.briefOutline = briefOutline;
        this.notation = notation;
        this.representationOptions = representationOptions;
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
    public String getNotation() {
        return notation;
    }

    public void setNotation(String notation) {
        this.notation = notation;
    }
    public String getRepresentationoptions() {
        return representationOptions;
    }

    public void setRepresentationoptions(String representationOptions) {
        this.representationOptions = representationOptions;
    }


}