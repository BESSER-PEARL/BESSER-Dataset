





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Property extends VariableDeclaration {

    private boolean derived;





    private applauseDsl_TypeDescription applausedsl_typedescription;




    private applauseDsl_Entity applausedsl_entity;


    public applauseDsl_Property(
        boolean derived    ) {
        super(
        );
        this.derived = derived;
    }


    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }

    public applauseDsl_TypeDescription getApplausedsl_typedescription() {
        return applausedsl_typedescription;
    }

    public void setApplausedsl_typedescription(applauseDsl_TypeDescription applausedsl_typedescription) {
        this.applausedsl_typedescription = applausedsl_typedescription;
    }
    public applauseDsl_Entity getApplausedsl_entity() {
        return applausedsl_entity;
    }

    public void setApplausedsl_entity(applauseDsl_Entity applausedsl_entity) {
        this.applausedsl_entity = applausedsl_entity;
    }

}