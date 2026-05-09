





import java.util.List;
import java.util.ArrayList;

public class ecore_EReference extends EStructuralFeature {

    private String container;
    private String containment;
    private String resolveProxies;



    public ecore_EReference(
        String container,        String containment,        String resolveProxies    ) {
        super(
        );
        this.container = container;
        this.containment = containment;
        this.resolveProxies = resolveProxies;
    }


    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }
    public String getContainment() {
        return containment;
    }

    public void setContainment(String containment) {
        this.containment = containment;
    }
    public String getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(String resolveProxies) {
        this.resolveProxies = resolveProxies;
    }


}