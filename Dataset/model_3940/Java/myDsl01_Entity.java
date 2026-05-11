





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Entity  {

    private String name;
    private boolean abstract;





    private myDsl01_Entity mydsl01_entity;




    private myDsl01_Model mydsl01_model;


    public myDsl01_Entity(
        String name,        boolean abstract    ) {
        this.name = name;
        this.abstract = abstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public myDsl01_Entity getMydsl01_entity() {
        return mydsl01_entity;
    }

    public void setMydsl01_entity(myDsl01_Entity mydsl01_entity) {
        this.mydsl01_entity = mydsl01_entity;
    }
    public myDsl01_Model getMydsl01_model() {
        return mydsl01_model;
    }

    public void setMydsl01_model(myDsl01_Model mydsl01_model) {
        this.mydsl01_model = mydsl01_model;
    }

}