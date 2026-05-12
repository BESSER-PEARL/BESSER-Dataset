





import java.util.List;
import java.util.ArrayList;

public class Scheduler  {

    private None newQueue;
    private None ioQueue;
    private None readyQueue;
    private int identifier;





    private Operating_System operating_system;


    public Scheduler(
        None newQueue,        None ioQueue,        None readyQueue,        int identifier    ) {
        this.newQueue = newQueue;
        this.ioQueue = ioQueue;
        this.readyQueue = readyQueue;
        this.identifier = identifier;
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
    public None getReadyqueue() {
        return readyQueue;
    }

    public void setReadyqueue(None readyQueue) {
        this.readyQueue = readyQueue;
    }
    public int getIdentifier() {
        return identifier;
    }

    public void setIdentifier(int identifier) {
        this.identifier = identifier;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}