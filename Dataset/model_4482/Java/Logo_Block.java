





import java.util.List;
import java.util.ArrayList;

public class Logo_Block extends ControlStructure {






    private List<Logo_Instruction> logo_instructions;




    private Logo_Procedure logo_procedure;




    private Logo_If logo_if;


    public Logo_Block(
    ) {
        super(
        );
        this.logo_instructions = new ArrayList<>();
    }

    public Logo_Block(
        ArrayList<Logo_Instruction> logo_instructions    ) {
        this.logo_instructions = logo_instructions;
    }


    public List<Logo_Instruction> getLogo_instructions() {
        return logo_instructions;
    }

    public void addLogo_instruction(Logo_instruction logo_instruction) {
        this.logo_instructions.add(logo_instruction);
    }
    public Logo_Procedure getLogo_procedure() {
        return logo_procedure;
    }

    public void setLogo_procedure(Logo_Procedure logo_procedure) {
        this.logo_procedure = logo_procedure;
    }
    public Logo_If getLogo_if() {
        return logo_if;
    }

    public void setLogo_if(Logo_If logo_if) {
        this.logo_if = logo_if;
    }

}