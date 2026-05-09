





import java.util.List;
import java.util.ArrayList;

public class express_core_UniqueRule extends TypeElement {

    private String position;





    private List<Attribute> attributes;




    private EntityType entitytype;


    public express_core_UniqueRule(
        String position    ) {
        super(
        );
        this.position = position;
        this.attributes = new ArrayList<>();
    }

    public express_core_UniqueRule(
        String position        ArrayList<Attribute> attributes    ) {
        this.position = position;
        this.attributes = attributes;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }
    public EntityType getEntitytype() {
        return entitytype;
    }

    public void setEntitytype(EntityType entitytype) {
        this.entitytype = entitytype;
    }

}