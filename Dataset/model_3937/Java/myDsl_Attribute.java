





import java.util.List;
import java.util.ArrayList;

public class myDsl_Attribute  {

    private String name;
    private boolean many;





    private myDsl_Entity mydsl_entity;




    private myDsl_Association mydsl_association;




    private myDsl_Type mydsl_type;


    public myDsl_Attribute(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }
    public myDsl_Association getMydsl_association() {
        return mydsl_association;
    }

    public void setMydsl_association(myDsl_Association mydsl_association) {
        this.mydsl_association = mydsl_association;
    }
    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}