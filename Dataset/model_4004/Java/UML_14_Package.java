





import java.util.List;
import java.util.ArrayList;

public class UML_14_Package extends NamedElement {






    private List<UML_14_Generalization> uml_14_generalizations;




    private List<UML_14_Package> uml_14_packages;




    private List<UML_14_Class> uml_14_classs;




    private List<UML_14_DataType> uml_14_datatypes;


    public UML_14_Package(
    ) {
        super(
        );
        this.uml_14_generalizations = new ArrayList<>();
        this.uml_14_packages = new ArrayList<>();
        this.uml_14_classs = new ArrayList<>();
        this.uml_14_datatypes = new ArrayList<>();
    }

    public UML_14_Package(
        ArrayList<UML_14_Generalization> uml_14_generalizations,        ArrayList<UML_14_Package> uml_14_packages,        ArrayList<UML_14_Class> uml_14_classs,        ArrayList<UML_14_DataType> uml_14_datatypes    ) {
        this.uml_14_generalizations = uml_14_generalizations;
        this.uml_14_packages = uml_14_packages;
        this.uml_14_classs = uml_14_classs;
        this.uml_14_datatypes = uml_14_datatypes;
    }


    public List<UML_14_Generalization> getUml_14_generalizations() {
        return uml_14_generalizations;
    }

    public void addUml_14_generalization(Uml_14_generalization uml_14_generalization) {
        this.uml_14_generalizations.add(uml_14_generalization);
    }
    public List<UML_14_Package> getUml_14_packages() {
        return uml_14_packages;
    }

    public void addUml_14_package(Uml_14_package uml_14_package) {
        this.uml_14_packages.add(uml_14_package);
    }
    public List<UML_14_Class> getUml_14_classs() {
        return uml_14_classs;
    }

    public void addUml_14_class(Uml_14_class uml_14_class) {
        this.uml_14_classs.add(uml_14_class);
    }
    public List<UML_14_DataType> getUml_14_datatypes() {
        return uml_14_datatypes;
    }

    public void addUml_14_datatype(Uml_14_datatype uml_14_datatype) {
        this.uml_14_datatypes.add(uml_14_datatype);
    }

}