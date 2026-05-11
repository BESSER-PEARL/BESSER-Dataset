





import java.util.List;
import java.util.ArrayList;

public class selflet_SelfLetProperty  {

    private String name;
    private String type;
    private String value;





    private selflet_TypeKnowledge selflet_typeknowledge;




    private selflet_GeneralKnowledge selflet_generalknowledge;


    public selflet_SelfLetProperty(
        String name,        String type,        String value    ) {
        this.name = name;
        this.type = type;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public selflet_TypeKnowledge getSelflet_typeknowledge() {
        return selflet_typeknowledge;
    }

    public void setSelflet_typeknowledge(selflet_TypeKnowledge selflet_typeknowledge) {
        this.selflet_typeknowledge = selflet_typeknowledge;
    }
    public selflet_GeneralKnowledge getSelflet_generalknowledge() {
        return selflet_generalknowledge;
    }

    public void setSelflet_generalknowledge(selflet_GeneralKnowledge selflet_generalknowledge) {
        this.selflet_generalknowledge = selflet_generalknowledge;
    }

}