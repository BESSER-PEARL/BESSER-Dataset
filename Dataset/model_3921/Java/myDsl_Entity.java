





import java.util.List;
import java.util.ArrayList;

public class myDsl_Entity extends Type {






    private myDsl_Entity mydsl_entity;




    private List<myDsl_Entity> mydsl_entitys;


    public myDsl_Entity(
    ) {
        super(
        );
        this.mydsl_entitys = new ArrayList<>();
    }

    public myDsl_Entity(
        ArrayList<myDsl_Entity> mydsl_entitys    ) {
        this.mydsl_entitys = mydsl_entitys;
    }


    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }
    public List<myDsl_Entity> getMydsl_entitys() {
        return mydsl_entitys;
    }

    public void addMydsl_entity(Mydsl_entity mydsl_entity) {
        this.mydsl_entitys.add(mydsl_entity);
    }

}