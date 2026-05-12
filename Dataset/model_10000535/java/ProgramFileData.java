





import java.util.List;
import java.util.ArrayList;

public class ProgramFileData  {

    private int memory;
    private None instructions;
    private String name;





    private JobFileData jobfiledata;




    private Instruction_Instruction_Interface instruction_instruction_interface;


    public ProgramFileData(
        int memory,        None instructions,        String name    ) {
        this.memory = memory;
        this.instructions = instructions;
        this.name = name;
    }


    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }
    public None getInstructions() {
        return instructions;
    }

    public void setInstructions(None instructions) {
        this.instructions = instructions;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public JobFileData getJobfiledata() {
        return jobfiledata;
    }

    public void setJobfiledata(JobFileData jobfiledata) {
        this.jobfiledata = jobfiledata;
    }
    public Instruction_Instruction_Interface getInstruction_instruction_interface() {
        return instruction_instruction_interface;
    }

    public void setInstruction_instruction_interface(Instruction_Instruction_Interface instruction_instruction_interface) {
        this.instruction_instruction_interface = instruction_instruction_interface;
    }

}