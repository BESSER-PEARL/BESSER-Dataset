





import java.util.List;
import java.util.ArrayList;

public class egraphs_EHyperEdge  {

    private String label;





    private egraphs_ENode egraphs_enode;




    private egraphs_ENode egraphs_enode;




    private egraphs_ENode egraphs_enode;




    private List<egraphs_ENode> egraphs_enodes;


    public egraphs_EHyperEdge(
        String label    ) {
        this.label = label;
        this.egraphs_enodes = new ArrayList<>();
    }

    public egraphs_EHyperEdge(
        String label        ArrayList<egraphs_ENode> egraphs_enodes    ) {
        this.label = label;
        this.egraphs_enodes = egraphs_enodes;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public egraphs_ENode getEgraphs_enode() {
        return egraphs_enode;
    }

    public void setEgraphs_enode(egraphs_ENode egraphs_enode) {
        this.egraphs_enode = egraphs_enode;
    }
    public egraphs_ENode getEgraphs_enode() {
        return egraphs_enode;
    }

    public void setEgraphs_enode(egraphs_ENode egraphs_enode) {
        this.egraphs_enode = egraphs_enode;
    }
    public egraphs_ENode getEgraphs_enode() {
        return egraphs_enode;
    }

    public void setEgraphs_enode(egraphs_ENode egraphs_enode) {
        this.egraphs_enode = egraphs_enode;
    }
    public List<egraphs_ENode> getEgraphs_enodes() {
        return egraphs_enodes;
    }

    public void addEgraphs_enode(Egraphs_enode egraphs_enode) {
        this.egraphs_enodes.add(egraphs_enode);
    }

}