





import java.util.List;
import java.util.ArrayList;

public class railway_Segment extends TrackElement {

    private int length;





    private List<railway_Semaphore> railway_semaphores;


    public railway_Segment(
        int length    ) {
        super(
        );
        this.length = length;
        this.railway_semaphores = new ArrayList<>();
    }

    public railway_Segment(
        int length        ArrayList<railway_Semaphore> railway_semaphores    ) {
        this.length = length;
        this.railway_semaphores = railway_semaphores;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public List<railway_Semaphore> getRailway_semaphores() {
        return railway_semaphores;
    }

    public void addRailway_semaphore(Railway_semaphore railway_semaphore) {
        this.railway_semaphores.add(railway_semaphore);
    }

}