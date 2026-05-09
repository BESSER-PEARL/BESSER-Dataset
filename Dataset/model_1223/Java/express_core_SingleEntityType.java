





import java.util.List;
import java.util.ArrayList;

public class express_core_SingleEntityType  {






    private List<ExplicitAttribute> explicitattributes;




    private ScopedId scopedid;




    private EntityType entitytype;




    private List<Attribute> attributes;


    public express_core_SingleEntityType(
    ) {
        this.explicitattributes = new ArrayList<>();
        this.attributes = new ArrayList<>();
    }

    public express_core_SingleEntityType(
        ArrayList<ExplicitAttribute> explicitattributes,        ArrayList<Attribute> attributes    ) {
        this.explicitattributes = explicitattributes;
        this.attributes = attributes;
    }


    public List<ExplicitAttribute> getExplicitattributes() {
        return explicitattributes;
    }

    public void addExplicitattribute(Explicitattribute explicitattribute) {
        this.explicitattributes.add(explicitattribute);
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
    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}