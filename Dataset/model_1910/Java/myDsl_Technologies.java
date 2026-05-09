





import java.util.List;
import java.util.ArrayList;

public class myDsl_Technologies  {






    private List<myDsl_EObject> mydsl_eobjects;




    private myDsl_Technology mydsl_technology;


    public myDsl_Technologies(
    ) {
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_Technologies(
        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.mydsl_eobjects = mydsl_eobjects;
    }


    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }
    public myDsl_Technology getMydsl_technology() {
        return mydsl_technology;
    }

    public void setMydsl_technology(myDsl_Technology mydsl_technology) {
        this.mydsl_technology = mydsl_technology;
    }

}