





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EReference extends EStructuralFeature {

    private boolean resolveProxies;
    private boolean container;
    private boolean containment;





    private List<activityecorelua_EAttribute> activityecorelua_eattributes;




    private activityecorelua_EReference activityecorelua_ereference;


    public activityecorelua_EReference(
        boolean resolveProxies,        boolean container,        boolean containment    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.containment = containment;
        this.activityecorelua_eattributes = new ArrayList<>();
    }

    public activityecorelua_EReference(
        boolean resolveProxies,        boolean container,        boolean containment        ArrayList<activityecorelua_EAttribute> activityecorelua_eattributes    ) {
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.containment = containment;
        this.activityecorelua_eattributes = activityecorelua_eattributes;
    }

    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }
    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }

    public List<activityecorelua_EAttribute> getActivityecorelua_eattributes() {
        return activityecorelua_eattributes;
    }

    public void addActivityecorelua_eattribute(Activityecorelua_eattribute activityecorelua_eattribute) {
        this.activityecorelua_eattributes.add(activityecorelua_eattribute);
    }
    public activityecorelua_EReference getActivityecorelua_ereference() {
        return activityecorelua_ereference;
    }

    public void setActivityecorelua_ereference(activityecorelua_EReference activityecorelua_ereference) {
        this.activityecorelua_ereference = activityecorelua_ereference;
    }

}