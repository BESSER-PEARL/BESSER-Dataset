





import java.util.List;
import java.util.ArrayList;

public class ram_Association extends NamedElement {






    private List<ram_AssociationEnd> ram_associationends;




    private ram_AssociationEnd ram_associationend;


    public ram_Association(
    ) {
        super(
        );
        this.ram_associationends = new ArrayList<>();
    }

    public ram_Association(
        ArrayList<ram_AssociationEnd> ram_associationends    ) {
        this.ram_associationends = ram_associationends;
    }


    public List<ram_AssociationEnd> getRam_associationends() {
        return ram_associationends;
    }

    public void addRam_associationend(Ram_associationend ram_associationend) {
        this.ram_associationends.add(ram_associationend);
    }
    public ram_AssociationEnd getRam_associationend() {
        return ram_associationend;
    }

    public void setRam_associationend(ram_AssociationEnd ram_associationend) {
        this.ram_associationend = ram_associationend;
    }

}