





import java.util.List;
import java.util.ArrayList;

public class surveillance_UnidentifiedObject extends MovingObject, ProbableElement {






    private List<surveillance_GunShot> surveillance_gunshots;




    private surveillance_GunShot surveillance_gunshot;


    public surveillance_UnidentifiedObject(
    ) {
        super(
        );
        this.surveillance_gunshots = new ArrayList<>();
    }

    public surveillance_UnidentifiedObject(
        ArrayList<surveillance_GunShot> surveillance_gunshots    ) {
        this.surveillance_gunshots = surveillance_gunshots;
    }


    public List<surveillance_GunShot> getSurveillance_gunshots() {
        return surveillance_gunshots;
    }

    public void addSurveillance_gunshot(Surveillance_gunshot surveillance_gunshot) {
        this.surveillance_gunshots.add(surveillance_gunshot);
    }
    public surveillance_GunShot getSurveillance_gunshot() {
        return surveillance_gunshot;
    }

    public void setSurveillance_gunshot(surveillance_GunShot surveillance_gunshot) {
        this.surveillance_gunshot = surveillance_gunshot;
    }

}