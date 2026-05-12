





import java.util.List;
import java.util.ArrayList;

public class Passenger  {

    private int DEST;
    private boolean waiting;
    private int START_FLOOR;
    private boolean traveling;
    private boolean readyToDie;
    private int WEIGHT;
    private int carNum;





    private Sim sim;


    public Passenger(
        int DEST,        boolean waiting,        int START_FLOOR,        boolean traveling,        boolean readyToDie,        int WEIGHT,        int carNum    ) {
        this.DEST = DEST;
        this.waiting = waiting;
        this.START_FLOOR = START_FLOOR;
        this.traveling = traveling;
        this.readyToDie = readyToDie;
        this.WEIGHT = WEIGHT;
        this.carNum = carNum;
    }


    public int getDest() {
        return DEST;
    }

    public void setDest(int DEST) {
        this.DEST = DEST;
    }
    public boolean getWaiting() {
        return waiting;
    }

    public void setWaiting(boolean waiting) {
        this.waiting = waiting;
    }
    public int getStart_floor() {
        return START_FLOOR;
    }

    public void setStart_floor(int START_FLOOR) {
        this.START_FLOOR = START_FLOOR;
    }
    public boolean getTraveling() {
        return traveling;
    }

    public void setTraveling(boolean traveling) {
        this.traveling = traveling;
    }
    public boolean getReadytodie() {
        return readyToDie;
    }

    public void setReadytodie(boolean readyToDie) {
        this.readyToDie = readyToDie;
    }
    public int getWeight() {
        return WEIGHT;
    }

    public void setWeight(int WEIGHT) {
        this.WEIGHT = WEIGHT;
    }
    public int getCarnum() {
        return carNum;
    }

    public void setCarnum(int carNum) {
        this.carNum = carNum;
    }

    public Sim getSim() {
        return sim;
    }

    public void setSim(Sim sim) {
        this.sim = sim;
    }

}