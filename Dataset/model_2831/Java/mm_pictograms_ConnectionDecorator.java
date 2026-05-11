





import java.util.List;
import java.util.ArrayList;

public class mm_pictograms_ConnectionDecorator extends Shape {

    private float location;
    private boolean locationRelative;





    private Connection connection;


    public mm_pictograms_ConnectionDecorator(
        float location,        boolean locationRelative    ) {
        super(
        );
        this.location = location;
        this.locationRelative = locationRelative;
    }


    public float getLocation() {
        return location;
    }

    public void setLocation(float location) {
        this.location = location;
    }
    public boolean getLocationrelative() {
        return locationRelative;
    }

    public void setLocationrelative(boolean locationRelative) {
        this.locationRelative = locationRelative;
    }

    public Connection getConnection() {
        return connection;
    }

    public void setConnection(Connection connection) {
        this.connection = connection;
    }

}