





import java.util.List;
import java.util.ArrayList;

public class ProgramFileData  {

    private int memory;
    private String name;
    private None instructions;



    public ProgramFileData(
        int memory,        String name,        None instructions    ) {
        this.memory = memory;
        this.name = name;
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
    public None getInstructions() {
        return instructions;
    }

    public void setInstructions(None instructions) {
        this.instructions = instructions;
    }


}