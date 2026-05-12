





import java.util.List;
import java.util.ArrayList;

public class Common_Behavior_LinkEnd extends ModelElement {






    private List<AttributeLink> attributelinks;




    private Link link;




    private Instance instance;


    public Common_Behavior_LinkEnd(
    ) {
        super(
        );
        this.attributelinks = new ArrayList<>();
    }

    public Common_Behavior_LinkEnd(
        ArrayList<AttributeLink> attributelinks    ) {
        this.attributelinks = attributelinks;
    }


    public List<AttributeLink> getAttributelinks() {
        return attributelinks;
    }

    public void addAttributelink(Attributelink attributelink) {
        this.attributelinks.add(attributelink);
    }
    public Link getLink() {
        return link;
    }

    public void setLink(Link link) {
        this.link = link;
    }
    public Instance getInstance() {
        return instance;
    }

    public void setInstance(Instance instance) {
        this.instance = instance;
    }

}