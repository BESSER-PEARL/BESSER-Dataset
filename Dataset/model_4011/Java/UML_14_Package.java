





import java.util.List;
import java.util.ArrayList;

public class UML_14_Package extends NamedElement {






    private List<UML_14_Association> uml_14_associations;




    private List<UML_14_Class> uml_14_classs;




    private List<UML_14_Generalization> uml_14_generalizations;




    private UML_14_Package uml_14_package;




    private List<UML_14_Enumeration> uml_14_enumerations;


    public UML_14_Package(
    ) {
        super(
        );
        this.uml_14_associations = new ArrayList<>();
        this.uml_14_classs = new ArrayList<>();
        this.uml_14_generalizations = new ArrayList<>();
        this.uml_14_enumerations = new ArrayList<>();
    }

    public UML_14_Package(
        ArrayList<UML_14_Association> uml_14_associations,        ArrayList<UML_14_Class> uml_14_classs,        ArrayList<UML_14_Generalization> uml_14_generalizations,        ArrayList<UML_14_Enumeration> uml_14_enumerations    ) {
        this.uml_14_associations = uml_14_associations;
        this.uml_14_classs = uml_14_classs;
        this.uml_14_generalizations = uml_14_generalizations;
        this.uml_14_enumerations = uml_14_enumerations;
    }


    public List<UML_14_Association> getUml_14_associations() {
        return uml_14_associations;
    }

    public void addUml_14_association(Uml_14_association uml_14_association) {
        this.uml_14_associations.add(uml_14_association);
    }
    public List<UML_14_Class> getUml_14_classs() {
        return uml_14_classs;
    }

    public void addUml_14_class(Uml_14_class uml_14_class) {
        this.uml_14_classs.add(uml_14_class);
    }
    public List<UML_14_Generalization> getUml_14_generalizations() {
        return uml_14_generalizations;
    }

    public void addUml_14_generalization(Uml_14_generalization uml_14_generalization) {
        this.uml_14_generalizations.add(uml_14_generalization);
    }
    public UML_14_Package getUml_14_package() {
        return uml_14_package;
    }

    public void setUml_14_package(UML_14_Package uml_14_package) {
        this.uml_14_package = uml_14_package;
    }
    public List<UML_14_Enumeration> getUml_14_enumerations() {
        return uml_14_enumerations;
    }

    public void addUml_14_enumeration(Uml_14_enumeration uml_14_enumeration) {
        this.uml_14_enumerations.add(uml_14_enumeration);
    }

}