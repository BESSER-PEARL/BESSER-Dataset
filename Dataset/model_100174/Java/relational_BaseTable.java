





import java.util.List;
import java.util.ArrayList;

public class relational_BaseTable extends Table {






    private List<relational_ForeignKey> relational_foreignkeys;




    private relational_PrimaryKey relational_primarykey;




    private relational_PrimaryKey relational_primarykey;




    private List<relational_UniqueConstraint> relational_uniqueconstraints;




    private relational_UniqueConstraint relational_uniqueconstraint;




    private relational_ForeignKey relational_foreignkey;


    public relational_BaseTable(
    ) {
        super(
        );
        this.relational_foreignkeys = new ArrayList<>();
        this.relational_uniqueconstraints = new ArrayList<>();
    }

    public relational_BaseTable(
        ArrayList<relational_ForeignKey> relational_foreignkeys,        ArrayList<relational_UniqueConstraint> relational_uniqueconstraints    ) {
        this.relational_foreignkeys = relational_foreignkeys;
        this.relational_uniqueconstraints = relational_uniqueconstraints;
    }


    public List<relational_ForeignKey> getRelational_foreignkeys() {
        return relational_foreignkeys;
    }

    public void addRelational_foreignkey(Relational_foreignkey relational_foreignkey) {
        this.relational_foreignkeys.add(relational_foreignkey);
    }
    public relational_PrimaryKey getRelational_primarykey() {
        return relational_primarykey;
    }

    public void setRelational_primarykey(relational_PrimaryKey relational_primarykey) {
        this.relational_primarykey = relational_primarykey;
    }
    public relational_PrimaryKey getRelational_primarykey() {
        return relational_primarykey;
    }

    public void setRelational_primarykey(relational_PrimaryKey relational_primarykey) {
        this.relational_primarykey = relational_primarykey;
    }
    public List<relational_UniqueConstraint> getRelational_uniqueconstraints() {
        return relational_uniqueconstraints;
    }

    public void addRelational_uniqueconstraint(Relational_uniqueconstraint relational_uniqueconstraint) {
        this.relational_uniqueconstraints.add(relational_uniqueconstraint);
    }
    public relational_UniqueConstraint getRelational_uniqueconstraint() {
        return relational_uniqueconstraint;
    }

    public void setRelational_uniqueconstraint(relational_UniqueConstraint relational_uniqueconstraint) {
        this.relational_uniqueconstraint = relational_uniqueconstraint;
    }
    public relational_ForeignKey getRelational_foreignkey() {
        return relational_foreignkey;
    }

    public void setRelational_foreignkey(relational_ForeignKey relational_foreignkey) {
        this.relational_foreignkey = relational_foreignkey;
    }

}