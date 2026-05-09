





import java.util.List;
import java.util.ArrayList;

public class myDsl_Entities  {






    private List<myDsl_EObject> mydsl_eobjects;




    private myDsl_Entity mydsl_entity;


    public myDsl_Entities(
    ) {
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_Entities(
        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.mydsl_eobjects = mydsl_eobjects;
    }


    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }
    public myDsl_Entity getMydsl_entity() {
        return mydsl_entity;
    }

    public void setMydsl_entity(myDsl_Entity mydsl_entity) {
        this.mydsl_entity = mydsl_entity;
    }

}