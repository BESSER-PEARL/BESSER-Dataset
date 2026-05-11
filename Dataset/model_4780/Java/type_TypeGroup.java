





import java.util.List;
import java.util.ArrayList;

public class type_TypeGroup  {

    private String uid;
    private String name;





    private List<type_Relationship> type_relationships;


    public type_TypeGroup(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
        this.type_relationships = new ArrayList<>();
    }

    public type_TypeGroup(
        String uid,        String name        ArrayList<type_Relationship> type_relationships    ) {
        this.uid = uid;
        this.name = name;
        this.type_relationships = type_relationships;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<type_Relationship> getType_relationships() {
        return type_relationships;
    }

    public void addType_relationship(Type_relationship type_relationship) {
        this.type_relationships.add(type_relationship);
    }

}