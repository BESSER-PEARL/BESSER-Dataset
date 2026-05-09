





import java.util.List;
import java.util.ArrayList;

public class express_core_Attribute extends TypeElement {

    private String position;
    private String isAbstract;





    private SingleEntityType singleentitytype;




    private AttributeType attributetype;




    private List<EntityType> entitytypes;


    public express_core_Attribute(
        String position,        String isAbstract    ) {
        super(
        );
        this.position = position;
        this.isAbstract = isAbstract;
        this.entitytypes = new ArrayList<>();
    }

    public express_core_Attribute(
        String position,        String isAbstract        ArrayList<EntityType> entitytypes    ) {
        this.position = position;
        this.isAbstract = isAbstract;
        this.entitytypes = entitytypes;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public SingleEntityType getSingleentitytype() {
        return singleentitytype;
    }

    public void setSingleentitytype(SingleEntityType singleentitytype) {
        this.singleentitytype = singleentitytype;
    }
    public AttributeType getAttributetype() {
        return attributetype;
    }

    public void setAttributetype(AttributeType attributetype) {
        this.attributetype = attributetype;
    }
    public List<EntityType> getEntitytypes() {
        return entitytypes;
    }

    public void addEntitytype(Entitytype entitytype) {
        this.entitytypes.add(entitytype);
    }

}