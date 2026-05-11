





import java.util.List;
import java.util.ArrayList;

public class go_Chamada  {






    private List<go_EObject> go_eobjects;


    public go_Chamada(
    ) {
        this.go_eobjects = new ArrayList<>();
    }

    public go_Chamada(
        ArrayList<go_EObject> go_eobjects    ) {
        this.go_eobjects = go_eobjects;
    }


    public List<go_EObject> getGo_eobjects() {
        return go_eobjects;
    }

    public void addGo_eobject(Go_eobject go_eobject) {
        this.go_eobjects.add(go_eobject);
    }

}