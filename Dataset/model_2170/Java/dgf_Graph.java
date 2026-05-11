





import java.util.List;
import java.util.ArrayList;

public class dgf_Graph  {






    private List<dgf_DGraphElement> dgf_dgraphelements;


    public dgf_Graph(
    ) {
        this.dgf_dgraphelements = new ArrayList<>();
    }

    public dgf_Graph(
        ArrayList<dgf_DGraphElement> dgf_dgraphelements    ) {
        this.dgf_dgraphelements = dgf_dgraphelements;
    }


    public List<dgf_DGraphElement> getDgf_dgraphelements() {
        return dgf_dgraphelements;
    }

    public void addDgf_dgraphelement(Dgf_dgraphelement dgf_dgraphelement) {
        this.dgf_dgraphelements.add(dgf_dgraphelement);
    }

}