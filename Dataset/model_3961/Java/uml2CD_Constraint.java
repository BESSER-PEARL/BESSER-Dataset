





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Constraint extends PackageableElement {






    private uml2CD_Namespace uml2cd_namespace;




    private uml2CD_Namespace uml2cd_namespace;




    private List<uml2CD_Element> uml2cd_elements;


    public uml2CD_Constraint(
    ) {
        super(
        );
        this.uml2cd_elements = new ArrayList<>();
    }

    public uml2CD_Constraint(
        ArrayList<uml2CD_Element> uml2cd_elements    ) {
        this.uml2cd_elements = uml2cd_elements;
    }


    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }
    public uml2CD_Namespace getUml2cd_namespace() {
        return uml2cd_namespace;
    }

    public void setUml2cd_namespace(uml2CD_Namespace uml2cd_namespace) {
        this.uml2cd_namespace = uml2cd_namespace;
    }
    public List<uml2CD_Element> getUml2cd_elements() {
        return uml2cd_elements;
    }

    public void addUml2cd_element(Uml2cd_element uml2cd_element) {
        this.uml2cd_elements.add(uml2cd_element);
    }

}