





import java.util.List;
import java.util.ArrayList;

public class express_core_Role  {






    private SizeConstraint sizeconstraint;




    private SizeConstraint sizeconstraint;




    private Relationship relationship;




    private List<EntityType> entitytypes;


    public express_core_Role(
    ) {
        this.entitytypes = new ArrayList<>();
    }

    public express_core_Role(
        ArrayList<EntityType> entitytypes    ) {
        this.entitytypes = entitytypes;
    }


    public SizeConstraint getSizeconstraint() {
        return sizeconstraint;
    }

    public void setSizeconstraint(SizeConstraint sizeconstraint) {
        this.sizeconstraint = sizeconstraint;
    }
    public SizeConstraint getSizeconstraint() {
        return sizeconstraint;
    }

    public void setSizeconstraint(SizeConstraint sizeconstraint) {
        this.sizeconstraint = sizeconstraint;
    }
    public Relationship getRelationship() {
        return relationship;
    }

    public void setRelationship(Relationship relationship) {
        this.relationship = relationship;
    }
    public List<EntityType> getEntitytypes() {
        return entitytypes;
    }

    public void addEntitytype(Entitytype entitytype) {
        this.entitytypes.add(entitytype);
    }

}