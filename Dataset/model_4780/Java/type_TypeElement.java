





import java.util.List;
import java.util.ArrayList;

public class type_TypeElement  {

    private String uid;
    private String name;





    private type_Relationship type_relationship;




    private type_Relationship type_relationship;




    private type_TypeGroup type_typegroup;


    public type_TypeElement(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
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

    public type_Relationship getType_relationship() {
        return type_relationship;
    }

    public void setType_relationship(type_Relationship type_relationship) {
        this.type_relationship = type_relationship;
    }
    public type_Relationship getType_relationship() {
        return type_relationship;
    }

    public void setType_relationship(type_Relationship type_relationship) {
        this.type_relationship = type_relationship;
    }
    public type_TypeGroup getType_typegroup() {
        return type_typegroup;
    }

    public void setType_typegroup(type_TypeGroup type_typegroup) {
        this.type_typegroup = type_typegroup;
    }

}