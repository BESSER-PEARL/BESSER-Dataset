





import java.util.List;
import java.util.ArrayList;

public class UML2_ExpansionRegion extends StructuredActivityNode {

    private String mode;





    private UML2_ExpansionNode uml2_expansionnode;




    private List<UML2_ExpansionNode> uml2_expansionnodes;




    private List<UML2_ExpansionNode> uml2_expansionnodes;




    private UML2_ExpansionNode uml2_expansionnode;


    public UML2_ExpansionRegion(
        String mode    ) {
        super(
        );
        this.mode = mode;
        this.uml2_expansionnodes = new ArrayList<>();
        this.uml2_expansionnodes = new ArrayList<>();
    }

    public UML2_ExpansionRegion(
        String mode        ArrayList<UML2_ExpansionNode> uml2_expansionnodes,        ArrayList<UML2_ExpansionNode> uml2_expansionnodes    ) {
        this.mode = mode;
        this.uml2_expansionnodes = uml2_expansionnodes;
        this.uml2_expansionnodes = uml2_expansionnodes;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public UML2_ExpansionNode getUml2_expansionnode() {
        return uml2_expansionnode;
    }

    public void setUml2_expansionnode(UML2_ExpansionNode uml2_expansionnode) {
        this.uml2_expansionnode = uml2_expansionnode;
    }
    public List<UML2_ExpansionNode> getUml2_expansionnodes() {
        return uml2_expansionnodes;
    }

    public void addUml2_expansionnode(Uml2_expansionnode uml2_expansionnode) {
        this.uml2_expansionnodes.add(uml2_expansionnode);
    }
    public List<UML2_ExpansionNode> getUml2_expansionnodes() {
        return uml2_expansionnodes;
    }

    public void addUml2_expansionnode(Uml2_expansionnode uml2_expansionnode) {
        this.uml2_expansionnodes.add(uml2_expansionnode);
    }
    public UML2_ExpansionNode getUml2_expansionnode() {
        return uml2_expansionnode;
    }

    public void setUml2_expansionnode(UML2_ExpansionNode uml2_expansionnode) {
        this.uml2_expansionnode = uml2_expansionnode;
    }

}