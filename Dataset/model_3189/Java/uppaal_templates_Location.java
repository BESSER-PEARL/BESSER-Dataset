





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Location extends visuals_PlanarElement, core_NamedElement, core_CommentableElement, visuals_ColoredElement {

    private String locationTimeKind;





    private Template template;


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

    public Template getTemplate() {
        return template;
    }

    public void setTemplate(Template template) {
        this.template = template;
    }

}