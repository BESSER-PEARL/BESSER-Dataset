





import java.util.List;
import java.util.ArrayList;

public class express_core_DomainRole extends Role {






    private EntityType entitytype;




    private ScopedId scopedid;


    public express_core_DomainRole(
    ) {
        super(
        );
    }



    public EntityType getEntitytype() {
        return entitytype;
    }

    public void setEntitytype(EntityType entitytype) {
        this.entitytype = entitytype;
    }
    public ScopedId getScopedid() {
        return scopedid;
    }

    public void setScopedid(ScopedId scopedid) {
        this.scopedid = scopedid;
    }

}