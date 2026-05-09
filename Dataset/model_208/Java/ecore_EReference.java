





import java.util.List;
import java.util.ArrayList;

public class ecore_EReference extends EStructuralFeature {

    private String resolveProxies;
    private String containment;
    private String container;



    public ecore_EReference(
        String resolveProxies,        String containment,        String container    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
    }


    public String getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(String resolveProxies) {
        this.resolveProxies = resolveProxies;
    }
    public String getContainment() {
        return containment;
    }

    public void setContainment(String containment) {
        this.containment = containment;
    }
    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }


}