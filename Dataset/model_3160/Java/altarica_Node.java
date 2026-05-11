





import java.util.List;
import java.util.ArrayList;

public class altarica_Node extends NamedElement {






    private List<altarica_Declaration> altarica_declarations;




    private List<altarica_Instruction> altarica_instructions;




    private List<altarica_LabeledTransition> altarica_labeledtransitions;


    public altarica_Node(
    ) {
        super(
        );
        this.altarica_declarations = new ArrayList<>();
        this.altarica_instructions = new ArrayList<>();
        this.altarica_labeledtransitions = new ArrayList<>();
    }

    public altarica_Node(
        ArrayList<altarica_Declaration> altarica_declarations,        ArrayList<altarica_Instruction> altarica_instructions,        ArrayList<altarica_LabeledTransition> altarica_labeledtransitions    ) {
        this.altarica_declarations = altarica_declarations;
        this.altarica_instructions = altarica_instructions;
        this.altarica_labeledtransitions = altarica_labeledtransitions;
    }


    public List<altarica_Declaration> getAltarica_declarations() {
        return altarica_declarations;
    }

    public void addAltarica_declaration(Altarica_declaration altarica_declaration) {
        this.altarica_declarations.add(altarica_declaration);
    }
    public List<altarica_Instruction> getAltarica_instructions() {
        return altarica_instructions;
    }

    public void addAltarica_instruction(Altarica_instruction altarica_instruction) {
        this.altarica_instructions.add(altarica_instruction);
    }
    public List<altarica_LabeledTransition> getAltarica_labeledtransitions() {
        return altarica_labeledtransitions;
    }

    public void addAltarica_labeledtransition(Altarica_labeledtransition altarica_labeledtransition) {
        this.altarica_labeledtransitions.add(altarica_labeledtransition);
    }

}