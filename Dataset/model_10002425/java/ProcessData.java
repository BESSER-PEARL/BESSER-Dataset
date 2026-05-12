





import java.util.List;
import java.util.ArrayList;

public class ProcessData  {

    private None instructions;
    private String startTime;
    private String name;
    private int memory;



    public ProcessData(
        None instructions,        String startTime,        String name,        int memory    ) {
        this.instructions = instructions;
        this.startTime = startTime;
        this.name = name;
        this.memory = memory;
    }


    public None getInstructions() {
        return instructions;
    }

    public void setInstructions(None instructions) {
        this.instructions = instructions;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
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