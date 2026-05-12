





import java.util.List;
import java.util.ArrayList;

public class Scheduler  {

    private None newQueue;
    private None ioQueue;
    private int identifier;
    private None readyQueue;





    private Operating_System operating_system;


    public Scheduler(
        None newQueue,        None ioQueue,        int identifier,        None readyQueue    ) {
        this.newQueue = newQueue;
        this.ioQueue = ioQueue;
        this.identifier = identifier;
        this.readyQueue = readyQueue;
    }


    public None getNewqueue() {
        return newQueue;
    }

    public void setNewqueue(None newQueue) {
        this.newQueue = newQueue;
    }
    public None getIoqueue() {
        return ioQueue;
    }

    public void setIoqueue(None ioQueue) {
        this.ioQueue = ioQueue;
    }
    public int getIdentifier() {
        return identifier;
    }

    public void setIdentifier(int identifier) {
        this.identifier = identifier;
    }
    public None getReadyqueue() {
        return readyQueue;
    }

    public void setReadyqueue(None readyQueue) {
        this.readyQueue = readyQueue;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}