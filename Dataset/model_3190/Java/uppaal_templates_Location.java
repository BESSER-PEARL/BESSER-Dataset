





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Location extends visuals_ColoredElement, core_CommentableElement, visuals_PlanarElement, core_NamedElement {

    private String locationTimeKind;





    private Expression expression;


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

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}