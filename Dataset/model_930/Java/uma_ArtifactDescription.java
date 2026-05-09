





import java.util.List;
import java.util.ArrayList;

public class uma_ArtifactDescription extends WorkProductDescription {

    private String representation;
    private String representationOptions;
    private String briefOutline;
    private String notation;



    public uma_ArtifactDescription(
        String representation,        String representationOptions,        String briefOutline,        String notation    ) {
        super(
        );
        this.representation = representation;
        this.representationOptions = representationOptions;
        this.briefOutline = briefOutline;
        this.notation = notation;
    }


    public String getRepresentation() {
        return representation;
    }

    public void setRepresentation(String representation) {
        this.representation = representation;
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
    public String getNotation() {
        return notation;
    }

    public void setNotation(String notation) {
        this.notation = notation;
    }


}