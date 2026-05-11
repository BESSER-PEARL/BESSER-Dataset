





import java.util.List;
import java.util.ArrayList;

public class behaviour_EntityClass  {

    private String entityName;





    private List<behaviour_AttributeClass> behaviour_attributeclasss;


    public behaviour_EntityClass(
        String entityName    ) {
        this.entityName = entityName;
        this.behaviour_attributeclasss = new ArrayList<>();
    }

    public behaviour_EntityClass(
        String entityName        ArrayList<behaviour_AttributeClass> behaviour_attributeclasss    ) {
        this.entityName = entityName;
        this.behaviour_attributeclasss = behaviour_attributeclasss;
    }

    public String getEntityname() {
        return entityName;
    }

    public void setEntityname(String entityName) {
        this.entityName = entityName;
    }

    public List<behaviour_AttributeClass> getBehaviour_attributeclasss() {
        return behaviour_attributeclasss;
    }

    public void addBehaviour_attributeclass(Behaviour_attributeclass behaviour_attributeclass) {
        this.behaviour_attributeclasss.add(behaviour_attributeclass);
    }

}