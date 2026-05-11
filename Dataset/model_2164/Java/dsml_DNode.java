





import java.util.List;
import java.util.ArrayList;

public class dsml_DNode extends DContainedElement, DClassElement, DGraphElement {

    private boolean pointOfView;
    private String pointOfViewName;





    private List<dsml_DNode> dsml_dnodes;




    private dsml_DEdge dsml_dedge;




    private List<dsml_DEdge> dsml_dedges;




    private dsml_DNode dsml_dnode;




    private dsml_DEdge dsml_dedge;


    public dsml_DNode(
        boolean pointOfView,        String pointOfViewName    ) {
        super(
        );
        this.pointOfView = pointOfView;
        this.pointOfViewName = pointOfViewName;
        this.dsml_dnodes = new ArrayList<>();
        this.dsml_dedges = new ArrayList<>();
    }

    public dsml_DNode(
        boolean pointOfView,        String pointOfViewName        ArrayList<dsml_DNode> dsml_dnodes,        ArrayList<dsml_DEdge> dsml_dedges    ) {
        this.pointOfView = pointOfView;
        this.pointOfViewName = pointOfViewName;
        this.dsml_dnodes = dsml_dnodes;
        this.dsml_dedges = dsml_dedges;
    }

    public boolean getPointofview() {
        return pointOfView;
    }

    public void setPointofview(boolean pointOfView) {
        this.pointOfView = pointOfView;
    }
    public String getPointofviewname() {
        return pointOfViewName;
    }

    public void setPointofviewname(String pointOfViewName) {
        this.pointOfViewName = pointOfViewName;
    }

    public List<dsml_DNode> getDsml_dnodes() {
        return dsml_dnodes;
    }

    public void addDsml_dnode(Dsml_dnode dsml_dnode) {
        this.dsml_dnodes.add(dsml_dnode);
    }
    public dsml_DEdge getDsml_dedge() {
        return dsml_dedge;
    }

    public void setDsml_dedge(dsml_DEdge dsml_dedge) {
        this.dsml_dedge = dsml_dedge;
    }
    public List<dsml_DEdge> getDsml_dedges() {
        return dsml_dedges;
    }

    public void addDsml_dedge(Dsml_dedge dsml_dedge) {
        this.dsml_dedges.add(dsml_dedge);
    }
    public dsml_DNode getDsml_dnode() {
        return dsml_dnode;
    }

    public void setDsml_dnode(dsml_DNode dsml_dnode) {
        this.dsml_dnode = dsml_dnode;
    }
    public dsml_DEdge getDsml_dedge() {
        return dsml_dedge;
    }

    public void setDsml_dedge(dsml_DEdge dsml_dedge) {
        this.dsml_dedge = dsml_dedge;
    }

}