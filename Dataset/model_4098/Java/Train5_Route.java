





import java.util.List;
import java.util.ArrayList;

public class Train5_Route extends NamedElement {

    private String speed;
    private String currentIndex;
    private String leftOver;





    private Train5_TrackElement train5_trackelement;




    private List<Train5_RoutePart> train5_routeparts;


    public Train5_Route(
        String speed,        String currentIndex,        String leftOver    ) {
        super(
        );
        this.speed = speed;
        this.currentIndex = currentIndex;
        this.leftOver = leftOver;
        this.train5_routeparts = new ArrayList<>();
    }

    public Train5_Route(
        String speed,        String currentIndex,        String leftOver        ArrayList<Train5_RoutePart> train5_routeparts    ) {
        this.speed = speed;
        this.currentIndex = currentIndex;
        this.leftOver = leftOver;
        this.train5_routeparts = train5_routeparts;
    }

    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getCurrentindex() {
        return currentIndex;
    }

    public void setCurrentindex(String currentIndex) {
        this.currentIndex = currentIndex;
    }
    public String getLeftover() {
        return leftOver;
    }

    public void setLeftover(String leftOver) {
        this.leftOver = leftOver;
    }

    public Train5_TrackElement getTrain5_trackelement() {
        return train5_trackelement;
    }

    public void setTrain5_trackelement(Train5_TrackElement train5_trackelement) {
        this.train5_trackelement = train5_trackelement;
    }
    public List<Train5_RoutePart> getTrain5_routeparts() {
        return train5_routeparts;
    }

    public void addTrain5_routepart(Train5_routepart train5_routepart) {
        this.train5_routeparts.add(train5_routepart);
    }

}