





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Variable extends ConnectableElement, MultiplicityElement {

    private String scope;
    private String activityScope;



    public UMLModel_Variable(
        String scope,        String activityScope    ) {
        super(
        );
        this.scope = scope;
        this.activityScope = activityScope;
    }


    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }
    public String getActivityscope() {
        return activityScope;
    }

    public void setActivityscope(String activityScope) {
        this.activityScope = activityScope;
    }


}