





import java.util.List;
import java.util.ArrayList;

public class org_structure_Constraint extends NamedElement {

    private String language;
    private String stereotype;





    private behavior_Expression behavior_expression;


    public org_structure_Constraint(
        String language,        String stereotype    ) {
        super(
        );
        this.language = language;
        this.stereotype = stereotype;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}