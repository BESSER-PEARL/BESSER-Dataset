





import java.util.List;
import java.util.ArrayList;

public class UML_14_Association extends GeneralizableElement, Relationship {






    private UML_14_AssociationEnd uml_14_associationend;




    private List<UML_14_AssociationEnd> uml_14_associationends;


    public UML_14_Association(
    ) {
        super(
        );
        this.uml_14_associationends = new ArrayList<>();
    }

    public UML_14_Association(
        ArrayList<UML_14_AssociationEnd> uml_14_associationends    ) {
        this.uml_14_associationends = uml_14_associationends;
    }


    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }
    public List<UML_14_AssociationEnd> getUml_14_associationends() {
        return uml_14_associationends;
    }

    public void addUml_14_associationend(Uml_14_associationend uml_14_associationend) {
        this.uml_14_associationends.add(uml_14_associationend);
    }

}