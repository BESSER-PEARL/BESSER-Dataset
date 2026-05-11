





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ProcDeclaration extends Instruction {

    private String name;





    private List<kmLogo_ProcCall> kmlogo_proccalls;




    private List<kmLogo_Instruction> kmlogo_instructions;




    private kmLogo_ProcCall kmlogo_proccall;


    public kmLogo_ProcDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.kmlogo_proccalls = new ArrayList<>();
        this.kmlogo_instructions = new ArrayList<>();
    }

    public kmLogo_ProcDeclaration(
        String name        ArrayList<kmLogo_ProcCall> kmlogo_proccalls,        ArrayList<kmLogo_Instruction> kmlogo_instructions    ) {
        this.name = name;
        this.kmlogo_proccalls = kmlogo_proccalls;
        this.kmlogo_instructions = kmlogo_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<kmLogo_ProcCall> getKmlogo_proccalls() {
        return kmlogo_proccalls;
    }

    public void addKmlogo_proccall(Kmlogo_proccall kmlogo_proccall) {
        this.kmlogo_proccalls.add(kmlogo_proccall);
    }
    public List<kmLogo_Instruction> getKmlogo_instructions() {
        return kmlogo_instructions;
    }

    public void addKmlogo_instruction(Kmlogo_instruction kmlogo_instruction) {
        this.kmlogo_instructions.add(kmlogo_instruction);
    }
    public kmLogo_ProcCall getKmlogo_proccall() {
        return kmlogo_proccall;
    }

    public void setKmlogo_proccall(kmLogo_ProcCall kmlogo_proccall) {
        this.kmlogo_proccall = kmlogo_proccall;
    }

}