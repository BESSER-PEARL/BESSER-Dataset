





import java.util.List;
import java.util.ArrayList;

public class relational_BaseTable extends Table {






    private List<relational_ForeignKey> relational_foreignkeys;




    private relational_ForeignKey relational_foreignkey;


    public relational_BaseTable(
    ) {
        super(
        );
        this.relational_foreignkeys = new ArrayList<>();
    }

    public relational_BaseTable(
        ArrayList<relational_ForeignKey> relational_foreignkeys    ) {
        this.relational_foreignkeys = relational_foreignkeys;
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

}