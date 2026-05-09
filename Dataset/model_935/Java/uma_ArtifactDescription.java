





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String representationOptions;
    private String briefOutline;
    private String representation;
    private String notation;



    public uma_ArtifactDescription(
        String representationOptions,        String briefOutline,        String representation,        String notation    ) {
        super(
        );
        this.representationOptions = representationOptions;
        this.briefOutline = briefOutline;
        this.representation = representation;
        this.notation = notation;
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


}