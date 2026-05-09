





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ExpansionRegion extends StructuredActivityNode {

    private String mode;





    private List<UML2WithID_ExpansionNode> uml2withid_expansionnodes;




    private UML2WithID_ExpansionNode uml2withid_expansionnode;




    private List<UML2WithID_ExpansionNode> uml2withid_expansionnodes;




    private UML2WithID_ExpansionNode uml2withid_expansionnode;


    public UML2WithID_ExpansionRegion(
        String mode    ) {
        super(
        );
        this.mode = mode;
        this.uml2withid_expansionnodes = new ArrayList<>();
        this.uml2withid_expansionnodes = new ArrayList<>();
    }

    public UML2WithID_ExpansionRegion(
        String mode        ArrayList<UML2WithID_ExpansionNode> uml2withid_expansionnodes,        ArrayList<UML2WithID_ExpansionNode> uml2withid_expansionnodes    ) {
        this.mode = mode;
        this.uml2withid_expansionnodes = uml2withid_expansionnodes;
        this.uml2withid_expansionnodes = uml2withid_expansionnodes;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public List<UML2WithID_ExpansionNode> getUml2withid_expansionnodes() {
        return uml2withid_expansionnodes;
    }

    public void addUml2withid_expansionnode(Uml2withid_expansionnode uml2withid_expansionnode) {
        this.uml2withid_expansionnodes.add(uml2withid_expansionnode);
    }
    public UML2WithID_ExpansionNode getUml2withid_expansionnode() {
        return uml2withid_expansionnode;
    }

    public void setUml2withid_expansionnode(UML2WithID_ExpansionNode uml2withid_expansionnode) {
        this.uml2withid_expansionnode = uml2withid_expansionnode;
    }
    public List<UML2WithID_ExpansionNode> getUml2withid_expansionnodes() {
        return uml2withid_expansionnodes;
    }

    public void addUml2withid_expansionnode(Uml2withid_expansionnode uml2withid_expansionnode) {
        this.uml2withid_expansionnodes.add(uml2withid_expansionnode);
    }
    public UML2WithID_ExpansionNode getUml2withid_expansionnode() {
        return uml2withid_expansionnode;
    }

    public void setUml2withid_expansionnode(UML2WithID_ExpansionNode uml2withid_expansionnode) {
        this.uml2withid_expansionnode = uml2withid_expansionnode;
    }

}