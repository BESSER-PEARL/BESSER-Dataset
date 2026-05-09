





import java.util.List;
import java.util.ArrayList;

public class uml_ExpansionRegion extends StructuredActivityNode {

    private String mode;





    private List<uml_ExpansionNode> uml_expansionnodes;




    private List<uml_ExpansionNode> uml_expansionnodes;




    private uml_ExpansionNode uml_expansionnode;




    private uml_ExpansionNode uml_expansionnode;


    public uml_ExpansionRegion(
        String mode    ) {
        super(
        );
        this.mode = mode;
        this.uml_expansionnodes = new ArrayList<>();
        this.uml_expansionnodes = new ArrayList<>();
    }

    public uml_ExpansionRegion(
        String mode        ArrayList<uml_ExpansionNode> uml_expansionnodes,        ArrayList<uml_ExpansionNode> uml_expansionnodes    ) {
        this.mode = mode;
        this.uml_expansionnodes = uml_expansionnodes;
        this.uml_expansionnodes = uml_expansionnodes;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public List<uml_ExpansionNode> getUml_expansionnodes() {
        return uml_expansionnodes;
    }

    public void addUml_expansionnode(Uml_expansionnode uml_expansionnode) {
        this.uml_expansionnodes.add(uml_expansionnode);
    }
    public List<uml_ExpansionNode> getUml_expansionnodes() {
        return uml_expansionnodes;
    }

    public void addUml_expansionnode(Uml_expansionnode uml_expansionnode) {
        this.uml_expansionnodes.add(uml_expansionnode);
    }
    public uml_ExpansionNode getUml_expansionnode() {
        return uml_expansionnode;
    }

    public void setUml_expansionnode(uml_ExpansionNode uml_expansionnode) {
        this.uml_expansionnode = uml_expansionnode;
    }
    public uml_ExpansionNode getUml_expansionnode() {
        return uml_expansionnode;
    }

    public void setUml_expansionnode(uml_ExpansionNode uml_expansionnode) {
        this.uml_expansionnode = uml_expansionnode;
    }

}