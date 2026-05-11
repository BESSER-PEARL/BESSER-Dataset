





import java.util.List;
import java.util.ArrayList;

public class simpleumltordbms_ClassToTable extends ToColumn, FromAttributeOwner, UmlToRdbmsModelElement {






    private simpleumltordbms_AssociationToForeignKey simpleumltordbms_associationtoforeignkey;




    private simpleumltordbms_AssociationToForeignKey simpleumltordbms_associationtoforeignkey;




    private List<simpleumltordbms_AssociationToForeignKey> simpleumltordbms_associationtoforeignkeys;


    public simpleumltordbms_ClassToTable(
    ) {
        super(
        );
        this.simpleumltordbms_associationtoforeignkeys = new ArrayList<>();
    }

    public simpleumltordbms_ClassToTable(
        ArrayList<simpleumltordbms_AssociationToForeignKey> simpleumltordbms_associationtoforeignkeys    ) {
        this.simpleumltordbms_associationtoforeignkeys = simpleumltordbms_associationtoforeignkeys;
    }


    public simpleumltordbms_AssociationToForeignKey getSimpleumltordbms_associationtoforeignkey() {
        return simpleumltordbms_associationtoforeignkey;
    }

    public void setSimpleumltordbms_associationtoforeignkey(simpleumltordbms_AssociationToForeignKey simpleumltordbms_associationtoforeignkey) {
        this.simpleumltordbms_associationtoforeignkey = simpleumltordbms_associationtoforeignkey;
    }
    public simpleumltordbms_AssociationToForeignKey getSimpleumltordbms_associationtoforeignkey() {
        return simpleumltordbms_associationtoforeignkey;
    }

    public void setSimpleumltordbms_associationtoforeignkey(simpleumltordbms_AssociationToForeignKey simpleumltordbms_associationtoforeignkey) {
        this.simpleumltordbms_associationtoforeignkey = simpleumltordbms_associationtoforeignkey;
    }
    public List<simpleumltordbms_AssociationToForeignKey> getSimpleumltordbms_associationtoforeignkeys() {
        return simpleumltordbms_associationtoforeignkeys;
    }

    public void addSimpleumltordbms_associationtoforeignkey(Simpleumltordbms_associationtoforeignkey simpleumltordbms_associationtoforeignkey) {
        this.simpleumltordbms_associationtoforeignkeys.add(simpleumltordbms_associationtoforeignkey);
    }

}