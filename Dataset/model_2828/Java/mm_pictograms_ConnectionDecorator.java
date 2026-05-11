





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_ConnectionDecorator extends Shape {

    private boolean locationRelative;
    private float location;



    public mm_pictograms_ConnectionDecorator(
        boolean locationRelative,        float location    ) {
        super(
        );
        this.locationRelative = locationRelative;
        this.location = location;
    }


    public boolean getLocationrelative() {
        return locationRelative;
    }

    public void setLocationrelative(boolean locationRelative) {
        this.locationRelative = locationRelative;
    }
    public float getLocation() {
        return location;
    }

    public void setLocation(float location) {
        this.location = location;
    }


}