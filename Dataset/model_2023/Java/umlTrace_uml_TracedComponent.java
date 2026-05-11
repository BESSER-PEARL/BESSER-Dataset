





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedComponent extends TracedClass {






    private List<uml_TracedComponentRealization> uml_tracedcomponentrealizations;




    private List<uml_TracedInterface> uml_tracedinterfaces;




    private List<uml_TracedPackageableElement> uml_tracedpackageableelements;




    private List<uml_TracedInterface> uml_tracedinterfaces;


    public umlTrace_uml_TracedComponent(
    ) {
        super(
        );
        this.uml_tracedcomponentrealizations = new ArrayList<>();
        this.uml_tracedinterfaces = new ArrayList<>();
        this.uml_tracedpackageableelements = new ArrayList<>();
        this.uml_tracedinterfaces = new ArrayList<>();
    }

    public umlTrace_uml_TracedComponent(
        ArrayList<uml_TracedComponentRealization> uml_tracedcomponentrealizations,        ArrayList<uml_TracedInterface> uml_tracedinterfaces,        ArrayList<uml_TracedPackageableElement> uml_tracedpackageableelements,        ArrayList<uml_TracedInterface> uml_tracedinterfaces    ) {
        this.uml_tracedcomponentrealizations = uml_tracedcomponentrealizations;
        this.uml_tracedinterfaces = uml_tracedinterfaces;
        this.uml_tracedpackageableelements = uml_tracedpackageableelements;
        this.uml_tracedinterfaces = uml_tracedinterfaces;
    }


    public List<uml_TracedComponentRealization> getUml_tracedcomponentrealizations() {
        return uml_tracedcomponentrealizations;
    }

    public void addUml_tracedcomponentrealization(Uml_tracedcomponentrealization uml_tracedcomponentrealization) {
        this.uml_tracedcomponentrealizations.add(uml_tracedcomponentrealization);
    }
    public List<uml_TracedInterface> getUml_tracedinterfaces() {
        return uml_tracedinterfaces;
    }

    public void addUml_tracedinterface(Uml_tracedinterface uml_tracedinterface) {
        this.uml_tracedinterfaces.add(uml_tracedinterface);
    }
    public List<uml_TracedPackageableElement> getUml_tracedpackageableelements() {
        return uml_tracedpackageableelements;
    }

    public void addUml_tracedpackageableelement(Uml_tracedpackageableelement uml_tracedpackageableelement) {
        this.uml_tracedpackageableelements.add(uml_tracedpackageableelement);
    }
    public List<uml_TracedInterface> getUml_tracedinterfaces() {
        return uml_tracedinterfaces;
    }

    public void addUml_tracedinterface(Uml_tracedinterface uml_tracedinterface) {
        this.uml_tracedinterfaces.add(uml_tracedinterface);
    }

}