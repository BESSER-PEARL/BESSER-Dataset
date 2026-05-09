





import java.util.List;
import java.util.ArrayList;

public class express_core_RangeRole extends Role {






    private InvertibleAttribute invertibleattribute;




    private ScopedId scopedid;




    private EntityType entitytype;


    public express_core_RangeRole(
    ) {
        super(
        );
    }



    public InvertibleAttribute getInvertibleattribute() {
        return invertibleattribute;
    }

    public void setInvertibleattribute(InvertibleAttribute invertibleattribute) {
        this.invertibleattribute = invertibleattribute;
    }
    public ScopedId getScopedid() {
        return scopedid;
    }

    public void setScopedid(ScopedId scopedid) {
        this.scopedid = scopedid;
    }
    public EntityType getEntitytype() {
        return entitytype;
    }

    public void setEntitytype(EntityType entitytype) {
        this.entitytype = entitytype;
    }

}