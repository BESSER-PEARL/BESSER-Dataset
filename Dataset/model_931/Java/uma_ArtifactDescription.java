





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String representation;
    private String notation;
    private String briefOutline;
    private String representationOptions;



    public uma_ArtifactDescription(
        String representation,        String notation,        String briefOutline,        String representationOptions    ) {
        super(
        );
        this.representation = representation;
        this.notation = notation;
        this.briefOutline = briefOutline;
        this.representationOptions = representationOptions;
    }


    public String getRepresentation() {
        return representation;
    }

    public void setRepresentation(String representation) {
        this.representation = representation;
    }
    public String getNotation() {
        return notation;
    }

    public void setNotation(String notation) {
        this.notation = notation;
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