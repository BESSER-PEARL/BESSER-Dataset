





import java.util.List;
import java.util.ArrayList;

public class dsml_DGraph  {






    private dsml_DNode dsml_dnode;




    private dsml_Diagraph dsml_diagraph;




    private List<dsml_DNode> dsml_dnodes;


    public dsml_DGraph(
    ) {
        this.dsml_dnodes = new ArrayList<>();
    }

    public dsml_DGraph(
        ArrayList<dsml_DNode> dsml_dnodes    ) {
        this.dsml_dnodes = dsml_dnodes;
    }


    public dsml_DNode getDsml_dnode() {
        return dsml_dnode;
    }

    public void setDsml_dnode(dsml_DNode dsml_dnode) {
        this.dsml_dnode = dsml_dnode;
    }
    public dsml_Diagraph getDsml_diagraph() {
        return dsml_diagraph;
    }

    public void setDsml_diagraph(dsml_Diagraph dsml_diagraph) {
        this.dsml_diagraph = dsml_diagraph;
    }
    public List<dsml_DNode> getDsml_dnodes() {
        return dsml_dnodes;
    }

    public void addDsml_dnode(Dsml_dnode dsml_dnode) {
        this.dsml_dnodes.add(dsml_dnode);
    }

}