





import java.util.List;
import java.util.ArrayList;

public class gremlin_CollectionDefinition extends TraversalElement {






    private gremlin_TypeDeclaration gremlin_typedeclaration;




    private List<gremlin_Instruction> gremlin_instructions;


    public gremlin_CollectionDefinition(
    ) {
        super(
        );
        this.gremlin_instructions = new ArrayList<>();
    }

    public gremlin_CollectionDefinition(
        ArrayList<gremlin_Instruction> gremlin_instructions    ) {
        this.gremlin_instructions = gremlin_instructions;
    }


    public gremlin_TypeDeclaration getGremlin_typedeclaration() {
        return gremlin_typedeclaration;
    }

    public void setGremlin_typedeclaration(gremlin_TypeDeclaration gremlin_typedeclaration) {
        this.gremlin_typedeclaration = gremlin_typedeclaration;
    }
    public List<gremlin_Instruction> getGremlin_instructions() {
        return gremlin_instructions;
    }

    public void addGremlin_instruction(Gremlin_instruction gremlin_instruction) {
        this.gremlin_instructions.add(gremlin_instruction);
    }

}