





import java.util.List;
import java.util.ArrayList;

public class UML2_Constraint extends PackageableElement {






    private UML2_Extend uml2_extend;




    private UML2_Namespace uml2_namespace;




    private List<UML2_Element> uml2_elements;




    private UML2_Namespace uml2_namespace;




    private UML2_Namespace uml2_namespace;




    private UML2_ParameterSet uml2_parameterset;


    public UML2_Constraint(
    ) {
        super(
        );
        this.uml2_elements = new ArrayList<>();
    }

    public UML2_Constraint(
        ArrayList<UML2_Element> uml2_elements    ) {
        this.uml2_elements = uml2_elements;
    }


    public UML2_Extend getUml2_extend() {
        return uml2_extend;
    }

    public void setUml2_extend(UML2_Extend uml2_extend) {
        this.uml2_extend = uml2_extend;
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public List<UML2_Element> getUml2_elements() {
        return uml2_elements;
    }

    public void addUml2_element(Uml2_element uml2_element) {
        this.uml2_elements.add(uml2_element);
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_ParameterSet getUml2_parameterset() {
        return uml2_parameterset;
    }

    public void setUml2_parameterset(UML2_ParameterSet uml2_parameterset) {
        this.uml2_parameterset = uml2_parameterset;
    }

}