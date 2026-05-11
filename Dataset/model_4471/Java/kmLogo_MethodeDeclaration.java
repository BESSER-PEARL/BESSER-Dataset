





import java.util.List;
import java.util.ArrayList;

public class kmLogo_MethodeDeclaration extends Instruction {

    private String name;





    private kmLogo_MethodeCall kmlogo_methodecall;




    private List<kmLogo_Instruction> kmlogo_instructions;




    private List<kmLogo_MethodeCall> kmlogo_methodecalls;


    public kmLogo_MethodeDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.kmlogo_instructions = new ArrayList<>();
        this.kmlogo_methodecalls = new ArrayList<>();
    }

    public kmLogo_MethodeDeclaration(
        String name        ArrayList<kmLogo_Instruction> kmlogo_instructions,        ArrayList<kmLogo_MethodeCall> kmlogo_methodecalls    ) {
        this.name = name;
        this.kmlogo_instructions = kmlogo_instructions;
        this.kmlogo_methodecalls = kmlogo_methodecalls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public kmLogo_MethodeCall getKmlogo_methodecall() {
        return kmlogo_methodecall;
    }

    public void setKmlogo_methodecall(kmLogo_MethodeCall kmlogo_methodecall) {
        this.kmlogo_methodecall = kmlogo_methodecall;
    }
    public List<kmLogo_Instruction> getKmlogo_instructions() {
        return kmlogo_instructions;
    }

    public void addKmlogo_instruction(Kmlogo_instruction kmlogo_instruction) {
        this.kmlogo_instructions.add(kmlogo_instruction);
    }
    public List<kmLogo_MethodeCall> getKmlogo_methodecalls() {
        return kmlogo_methodecalls;
    }

    public void addKmlogo_methodecall(Kmlogo_methodecall kmlogo_methodecall) {
        this.kmlogo_methodecalls.add(kmlogo_methodecall);
    }

}