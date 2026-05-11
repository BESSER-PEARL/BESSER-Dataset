





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Main  {






    private List<kmLogo_Instruction> kmlogo_instructions;




    private kmLogo_JavaProgram kmlogo_javaprogram;


    public kmLogo_Main(
    ) {
        this.kmlogo_instructions = new ArrayList<>();
    }

    public kmLogo_Main(
        ArrayList<kmLogo_Instruction> kmlogo_instructions    ) {
        this.kmlogo_instructions = kmlogo_instructions;
    }


    public List<kmLogo_Instruction> getKmlogo_instructions() {
        return kmlogo_instructions;
    }

    public void addKmlogo_instruction(Kmlogo_instruction kmlogo_instruction) {
        this.kmlogo_instructions.add(kmlogo_instruction);
    }
    public kmLogo_JavaProgram getKmlogo_javaprogram() {
        return kmlogo_javaprogram;
    }

    public void setKmlogo_javaprogram(kmLogo_JavaProgram kmlogo_javaprogram) {
        this.kmlogo_javaprogram = kmlogo_javaprogram;
    }

}