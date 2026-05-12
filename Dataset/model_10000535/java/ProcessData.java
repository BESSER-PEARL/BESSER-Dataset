





import java.util.List;
import java.util.ArrayList;

public class ProcessData  {

    private int memory;
    private String name;
    private String startTime;
    private None instructions;





    private Instruction_Instruction_Interface instruction_instruction_interface;


    public ProcessData(
        int memory,        String name,        String startTime,        None instructions    ) {
        this.memory = memory;
        this.name = name;
        this.startTime = startTime;
        this.instructions = instructions;
    }


    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public None getInstructions() {
        return instructions;
    }

    public void setInstructions(None instructions) {
        this.instructions = instructions;
    }

    public Instruction_Instruction_Interface getInstruction_instruction_interface() {
        return instruction_instruction_interface;
    }

    public void setInstruction_instruction_interface(Instruction_Instruction_Interface instruction_instruction_interface) {
        this.instruction_instruction_interface = instruction_instruction_interface;
    }

}