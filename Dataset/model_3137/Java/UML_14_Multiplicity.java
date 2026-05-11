





import java.util.List;
import java.util.ArrayList;

public class UML_14_Multiplicity  {






    private UML_14_StructuralFeature uml_14_structuralfeature;




    private UML_14_MultiplicityRange uml_14_multiplicityrange;




    private List<UML_14_MultiplicityRange> uml_14_multiplicityranges;




    private UML_14_AssociationEnd uml_14_associationend;


    public UML_14_Multiplicity(
    ) {
        this.uml_14_multiplicityranges = new ArrayList<>();
    }

    public UML_14_Multiplicity(
        ArrayList<UML_14_MultiplicityRange> uml_14_multiplicityranges    ) {
        this.uml_14_multiplicityranges = uml_14_multiplicityranges;
    }


    public UML_14_StructuralFeature getUml_14_structuralfeature() {
        return uml_14_structuralfeature;
    }

    public void setUml_14_structuralfeature(UML_14_StructuralFeature uml_14_structuralfeature) {
        this.uml_14_structuralfeature = uml_14_structuralfeature;
    }
    public UML_14_MultiplicityRange getUml_14_multiplicityrange() {
        return uml_14_multiplicityrange;
    }

    public void setUml_14_multiplicityrange(UML_14_MultiplicityRange uml_14_multiplicityrange) {
        this.uml_14_multiplicityrange = uml_14_multiplicityrange;
    }
    public List<UML_14_MultiplicityRange> getUml_14_multiplicityranges() {
        return uml_14_multiplicityranges;
    }

    public void addUml_14_multiplicityrange(Uml_14_multiplicityrange uml_14_multiplicityrange) {
        this.uml_14_multiplicityranges.add(uml_14_multiplicityrange);
    }
    public UML_14_AssociationEnd getUml_14_associationend() {
        return uml_14_associationend;
    }

    public void setUml_14_associationend(UML_14_AssociationEnd uml_14_associationend) {
        this.uml_14_associationend = uml_14_associationend;
    }

}