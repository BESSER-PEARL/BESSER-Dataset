





import java.util.List;
import java.util.ArrayList;

public class myDsl_PresentationLayer  {






    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_PresentationLayer(
    ) {
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_PresentationLayer(
        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.mydsl_eobjects = mydsl_eobjects;
    }


    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}