





import java.util.List;
import java.util.ArrayList;

public class myDsl_ComponentClass  {






    private myDsl_LogicStructure mydsl_logicstructure;




    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_ComponentClass(
    ) {
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_ComponentClass(
        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.mydsl_eobjects = mydsl_eobjects;
    }


    public myDsl_LogicStructure getMydsl_logicstructure() {
        return mydsl_logicstructure;
    }

    public void setMydsl_logicstructure(myDsl_LogicStructure mydsl_logicstructure) {
        this.mydsl_logicstructure = mydsl_logicstructure;
    }
    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}