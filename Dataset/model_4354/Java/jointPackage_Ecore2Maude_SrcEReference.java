





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEReference extends SrcEStructuralFeature {

    private boolean resolveProxies;
    private boolean containment;
    private boolean container;





    private jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference;


    public jointPackage_Ecore2Maude_SrcEReference(
        boolean resolveProxies,        boolean containment,        boolean container    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
    }


    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }

    public jointPackage_Ecore2Maude_SrcEReference getJointpackage_ecore2maude_srcereference() {
        return jointpackage_ecore2maude_srcereference;
    }

    public void setJointpackage_ecore2maude_srcereference(jointPackage_Ecore2Maude_SrcEReference jointpackage_ecore2maude_srcereference) {
        this.jointpackage_ecore2maude_srcereference = jointpackage_ecore2maude_srcereference;
    }

}