





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Location extends core_NamedElement, visuals_PlanarElement, visuals_ColoredElement, core_CommentableElement {

    private String locationTimeKind;



    public uppaal_templates_Location(
        String locationTimeKind    ) {
        super(
        );
        this.locationTimeKind = locationTimeKind;
    }


    public String getLocationtimekind() {
        return locationTimeKind;
    }

    public void setLocationtimekind(String locationTimeKind) {
        this.locationTimeKind = locationTimeKind;
    }


}