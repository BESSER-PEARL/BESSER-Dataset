





import java.util.List;
import java.util.ArrayList;

public class logo_ProcDeclaration extends Instruction {

    private String name;





    private List<logo_Instruction> logo_instructions;


    public logo_ProcDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.logo_instructions = new ArrayList<>();
    }

    public logo_ProcDeclaration(
        String name        ArrayList<logo_Instruction> logo_instructions    ) {
        this.name = name;
        this.logo_instructions = logo_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<logo_Instruction> getLogo_instructions() {
        return logo_instructions;
    }

    public void addLogo_instruction(Logo_instruction logo_instruction) {
        this.logo_instructions.add(logo_instruction);
    }

}