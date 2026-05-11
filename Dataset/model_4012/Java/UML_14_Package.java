





import java.util.List;
import java.util.ArrayList;

public class UML_14_Package extends NamedElement {






    private List<UML_14_Primitive> uml_14_primitives;




    private List<UML_14_Association> uml_14_associations;




    private UML_14_Package uml_14_package;


    public UML_14_Package(
    ) {
        super(
        );
        this.uml_14_primitives = new ArrayList<>();
        this.uml_14_associations = new ArrayList<>();
    }

    public UML_14_Package(
        ArrayList<UML_14_Primitive> uml_14_primitives,        ArrayList<UML_14_Association> uml_14_associations    ) {
        this.uml_14_primitives = uml_14_primitives;
        this.uml_14_associations = uml_14_associations;
    }


    public List<UML_14_Primitive> getUml_14_primitives() {
        return uml_14_primitives;
    }

    public void addUml_14_primitive(Uml_14_primitive uml_14_primitive) {
        this.uml_14_primitives.add(uml_14_primitive);
    }
    public List<UML_14_Association> getUml_14_associations() {
        return uml_14_associations;
    }

    public void addUml_14_association(Uml_14_association uml_14_association) {
        this.uml_14_associations.add(uml_14_association);
    }
    public UML_14_Package getUml_14_package() {
        return uml_14_package;
    }

    public void setUml_14_package(UML_14_Package uml_14_package) {
        this.uml_14_package = uml_14_package;
    }

}