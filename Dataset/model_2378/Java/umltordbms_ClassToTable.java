





import java.util.List;
import java.util.ArrayList;

public class umltordbms_ClassToTable extends ToColumn, FromAttributeOwner {

    private String name;





    private List<umltordbms_AssociationToForeignKey> umltordbms_associationtoforeignkeys;




    private umltordbms_AssociationToForeignKey umltordbms_associationtoforeignkey;




    private umltordbms_AssociationToForeignKey umltordbms_associationtoforeignkey;


    public umltordbms_ClassToTable(
        String name    ) {
        super(
        );
        this.name = name;
        this.umltordbms_associationtoforeignkeys = new ArrayList<>();
    }

    public umltordbms_ClassToTable(
        String name        ArrayList<umltordbms_AssociationToForeignKey> umltordbms_associationtoforeignkeys    ) {
        this.name = name;
        this.umltordbms_associationtoforeignkeys = umltordbms_associationtoforeignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<umltordbms_AssociationToForeignKey> getUmltordbms_associationtoforeignkeys() {
        return umltordbms_associationtoforeignkeys;
    }

    public void addUmltordbms_associationtoforeignkey(Umltordbms_associationtoforeignkey umltordbms_associationtoforeignkey) {
        this.umltordbms_associationtoforeignkeys.add(umltordbms_associationtoforeignkey);
    }
    public umltordbms_AssociationToForeignKey getUmltordbms_associationtoforeignkey() {
        return umltordbms_associationtoforeignkey;
    }

    public void setUmltordbms_associationtoforeignkey(umltordbms_AssociationToForeignKey umltordbms_associationtoforeignkey) {
        this.umltordbms_associationtoforeignkey = umltordbms_associationtoforeignkey;
    }
    public umltordbms_AssociationToForeignKey getUmltordbms_associationtoforeignkey() {
        return umltordbms_associationtoforeignkey;
    }

    public void setUmltordbms_associationtoforeignkey(umltordbms_AssociationToForeignKey umltordbms_associationtoforeignkey) {
        this.umltordbms_associationtoforeignkey = umltordbms_associationtoforeignkey;
    }

}