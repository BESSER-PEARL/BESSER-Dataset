





import java.util.List;
import java.util.ArrayList;

public class relational_Table extends ModelElement {

    private String name;





    private List<relational_ForeignKey> relational_foreignkeys;




    private relational_ForeignKey relational_foreignkey;




    private relational_ForeignKey relational_foreignkey;


    public relational_Table(
        String name    ) {
        super(
        );
        this.name = name;
        this.relational_foreignkeys = new ArrayList<>();
    }

    public relational_Table(
        String name        ArrayList<relational_ForeignKey> relational_foreignkeys    ) {
        this.name = name;
        this.relational_foreignkeys = relational_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<relational_ForeignKey> getRelational_foreignkeys() {
        return relational_foreignkeys;
    }

    public void addRelational_foreignkey(Relational_foreignkey relational_foreignkey) {
        this.relational_foreignkeys.add(relational_foreignkey);
    }
    public relational_ForeignKey getRelational_foreignkey() {
        return relational_foreignkey;
    }

    public void setRelational_foreignkey(relational_ForeignKey relational_foreignkey) {
        this.relational_foreignkey = relational_foreignkey;
    }
    public relational_ForeignKey getRelational_foreignkey() {
        return relational_foreignkey;
    }

    public void setRelational_foreignkey(relational_ForeignKey relational_foreignkey) {
        this.relational_foreignkey = relational_foreignkey;
    }

}