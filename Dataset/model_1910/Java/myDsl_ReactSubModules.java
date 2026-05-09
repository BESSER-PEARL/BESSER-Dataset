





import java.util.List;
import java.util.ArrayList;

public class myDsl_ReactSubModules  {






    private myDsl_ReactModules mydsl_reactmodules;




    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_ReactSubModules(
    ) {
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_ReactSubModules(
        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.mydsl_eobjects = mydsl_eobjects;
    }


    public myDsl_ReactModules getMydsl_reactmodules() {
        return mydsl_reactmodules;
    }

    public void setMydsl_reactmodules(myDsl_ReactModules mydsl_reactmodules) {
        this.mydsl_reactmodules = mydsl_reactmodules;
    }
    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}