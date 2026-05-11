





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_ClassToTable extends ToColumn, FromAttributeOwner {

    private String name;





    private List<uml2rdbms_AssociationToForeignKey> uml2rdbms_associationtoforeignkeys;




    private uml2rdbms_AssociationToForeignKey uml2rdbms_associationtoforeignkey;




    private uml2rdbms_AssociationToForeignKey uml2rdbms_associationtoforeignkey;


    public uml2rdbms_ClassToTable(
        String name    ) {
        super(
        );
        this.name = name;
        this.uml2rdbms_associationtoforeignkeys = new ArrayList<>();
    }

    public uml2rdbms_ClassToTable(
        String name        ArrayList<uml2rdbms_AssociationToForeignKey> uml2rdbms_associationtoforeignkeys    ) {
        this.name = name;
        this.uml2rdbms_associationtoforeignkeys = uml2rdbms_associationtoforeignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<uml2rdbms_AssociationToForeignKey> getUml2rdbms_associationtoforeignkeys() {
        return uml2rdbms_associationtoforeignkeys;
    }

    public void addUml2rdbms_associationtoforeignkey(Uml2rdbms_associationtoforeignkey uml2rdbms_associationtoforeignkey) {
        this.uml2rdbms_associationtoforeignkeys.add(uml2rdbms_associationtoforeignkey);
    }
    public uml2rdbms_AssociationToForeignKey getUml2rdbms_associationtoforeignkey() {
        return uml2rdbms_associationtoforeignkey;
    }

    public void setUml2rdbms_associationtoforeignkey(uml2rdbms_AssociationToForeignKey uml2rdbms_associationtoforeignkey) {
        this.uml2rdbms_associationtoforeignkey = uml2rdbms_associationtoforeignkey;
    }
    public uml2rdbms_AssociationToForeignKey getUml2rdbms_associationtoforeignkey() {
        return uml2rdbms_associationtoforeignkey;
    }

    public void setUml2rdbms_associationtoforeignkey(uml2rdbms_AssociationToForeignKey uml2rdbms_associationtoforeignkey) {
        this.uml2rdbms_associationtoforeignkey = uml2rdbms_associationtoforeignkey;
    }

}