





import java.util.List;
import java.util.ArrayList;

public class dgf_DNode extends DTypedElement, DGraphElement, DContainedElement {

    private String pointOfView;





    private dgf_DContainedElement dgf_dcontainedelement;




    private List<dgf_DVertex> dgf_dvertexs;




    private dgf_DVertex dgf_dvertex;




    private dgf_DVertex dgf_dvertex;


    public dgf_DNode(
        String pointOfView    ) {
        super(
        );
        this.pointOfView = pointOfView;
        this.dgf_dvertexs = new ArrayList<>();
    }

    public dgf_DNode(
        String pointOfView        ArrayList<dgf_DVertex> dgf_dvertexs    ) {
        this.pointOfView = pointOfView;
        this.dgf_dvertexs = dgf_dvertexs;
    }

    public String getPointofview() {
        return pointOfView;
    }

    public void setPointofview(String pointOfView) {
        this.pointOfView = pointOfView;
    }

    public dgf_DContainedElement getDgf_dcontainedelement() {
        return dgf_dcontainedelement;
    }

    public void setDgf_dcontainedelement(dgf_DContainedElement dgf_dcontainedelement) {
        this.dgf_dcontainedelement = dgf_dcontainedelement;
    }
    public List<dgf_DVertex> getDgf_dvertexs() {
        return dgf_dvertexs;
    }

    public void addDgf_dvertex(Dgf_dvertex dgf_dvertex) {
        this.dgf_dvertexs.add(dgf_dvertex);
    }
    public dgf_DVertex getDgf_dvertex() {
        return dgf_dvertex;
    }

    public void setDgf_dvertex(dgf_DVertex dgf_dvertex) {
        this.dgf_dvertex = dgf_dvertex;
    }
    public dgf_DVertex getDgf_dvertex() {
        return dgf_dvertex;
    }

    public void setDgf_dvertex(dgf_DVertex dgf_dvertex) {
        this.dgf_dvertex = dgf_dvertex;
    }

}