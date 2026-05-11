





import java.util.List;
import java.util.ArrayList;

public class gremlin_PropertyStep extends Step {

    private String name;





    private gremlin_Instruction gremlin_instruction;


    public gremlin_PropertyStep(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gremlin_Instruction getGremlin_instruction() {
        return gremlin_instruction;
    }

    public void setGremlin_instruction(gremlin_Instruction gremlin_instruction) {
        this.gremlin_instruction = gremlin_instruction;
    }

}