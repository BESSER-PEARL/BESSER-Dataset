





import java.util.List;
import java.util.ArrayList;

public class Operating_System  {

    private None hardDrive;
    private None memory;
    private None prompt;
    private None cpu;
    private None taskManager;
    private None clock;



    public Operating_System(
        None hardDrive,        None memory,        None prompt,        None cpu,        None taskManager,        None clock    ) {
        this.hardDrive = hardDrive;
        this.memory = memory;
        this.prompt = prompt;
        this.cpu = cpu;
        this.taskManager = taskManager;
        this.clock = clock;
    }


    public None getHarddrive() {
        return hardDrive;
    }

    public void setHarddrive(None hardDrive) {
        this.hardDrive = hardDrive;
    }
    public None getMemory() {
        return memory;
    }

    public void setMemory(None memory) {
        this.memory = memory;
    }
    public None getPrompt() {
        return prompt;
    }

    public void setPrompt(None prompt) {
        this.prompt = prompt;
    }
    public None getCpu() {
        return cpu;
    }

    public void setCpu(None cpu) {
        this.cpu = cpu;
    }
    public None getTaskmanager() {
        return taskManager;
    }

    public void setTaskmanager(None taskManager) {
        this.taskManager = taskManager;
    }
    public None getClock() {
        return clock;
    }

    public void setClock(None clock) {
        this.clock = clock;
    }


}