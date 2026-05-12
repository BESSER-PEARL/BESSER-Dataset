





import java.util.List;
import java.util.ArrayList;

public class ProgramFileData  {

    private None instructions;
    private String name;
    private int memory;



    public ProgramFileData(
        None instructions,        String name,        int memory    ) {
        this.instructions = instructions;
        this.name = name;
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
    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }


}