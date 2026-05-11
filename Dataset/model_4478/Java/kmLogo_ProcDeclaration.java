





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ProcDeclaration extends Instruction {

    private String name;





    private List<kmLogo_Instruction> kmlogo_instructions;


    public kmLogo_ProcDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.kmlogo_instructions = new ArrayList<>();
    }

    public kmLogo_ProcDeclaration(
        String name        ArrayList<kmLogo_Instruction> kmlogo_instructions    ) {
        this.name = name;
        this.kmlogo_instructions = kmlogo_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<kmLogo_Instruction> getKmlogo_instructions() {
        return kmlogo_instructions;
    }

    public void addKmlogo_instruction(Kmlogo_instruction kmlogo_instruction) {
        this.kmlogo_instructions.add(kmlogo_instruction);
    }

}