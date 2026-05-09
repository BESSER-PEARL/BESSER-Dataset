





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String notation;
    private String representationOptions;
    private String representation;
    private String briefOutline;



    public uma_ArtifactDescription(
        String notation,        String representationOptions,        String representation,        String briefOutline    ) {
        super(
        );
        this.notation = notation;
        this.representationOptions = representationOptions;
        this.representation = representation;
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


}