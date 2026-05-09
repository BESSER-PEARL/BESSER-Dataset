





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ExpansionRegion extends StructuredActivityNode {

    private String mode;





    private List<uml3_0_0_ExpansionNode> uml3_0_0_expansionnodes;




    private uml3_0_0_ExpansionNode uml3_0_0_expansionnode;




    private List<uml3_0_0_ExpansionNode> uml3_0_0_expansionnodes;




    private uml3_0_0_ExpansionNode uml3_0_0_expansionnode;


    public uml3_0_0_ExpansionRegion(
        String mode    ) {
        super(
        );
        this.mode = mode;
        this.uml3_0_0_expansionnodes = new ArrayList<>();
        this.uml3_0_0_expansionnodes = new ArrayList<>();
    }

    public uml3_0_0_ExpansionRegion(
        String mode        ArrayList<uml3_0_0_ExpansionNode> uml3_0_0_expansionnodes,        ArrayList<uml3_0_0_ExpansionNode> uml3_0_0_expansionnodes    ) {
        this.mode = mode;
        this.uml3_0_0_expansionnodes = uml3_0_0_expansionnodes;
        this.uml3_0_0_expansionnodes = uml3_0_0_expansionnodes;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public List<uml3_0_0_ExpansionNode> getUml3_0_0_expansionnodes() {
        return uml3_0_0_expansionnodes;
    }

    public void addUml3_0_0_expansionnode(Uml3_0_0_expansionnode uml3_0_0_expansionnode) {
        this.uml3_0_0_expansionnodes.add(uml3_0_0_expansionnode);
    }
    public uml3_0_0_ExpansionNode getUml3_0_0_expansionnode() {
        return uml3_0_0_expansionnode;
    }

    public void setUml3_0_0_expansionnode(uml3_0_0_ExpansionNode uml3_0_0_expansionnode) {
        this.uml3_0_0_expansionnode = uml3_0_0_expansionnode;
    }
    public List<uml3_0_0_ExpansionNode> getUml3_0_0_expansionnodes() {
        return uml3_0_0_expansionnodes;
    }

    public void addUml3_0_0_expansionnode(Uml3_0_0_expansionnode uml3_0_0_expansionnode) {
        this.uml3_0_0_expansionnodes.add(uml3_0_0_expansionnode);
    }
    public uml3_0_0_ExpansionNode getUml3_0_0_expansionnode() {
        return uml3_0_0_expansionnode;
    }

    public void setUml3_0_0_expansionnode(uml3_0_0_ExpansionNode uml3_0_0_expansionnode) {
        this.uml3_0_0_expansionnode = uml3_0_0_expansionnode;
    }

}