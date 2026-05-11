





import java.util.List;
import java.util.ArrayList;

public class railDsl_RouteObject  {

    private String speedLimit;
    private boolean error;



    public railDsl_RouteObject(
        String speedLimit,        boolean error    ) {
        this.speedLimit = speedLimit;
        this.error = error;
    }


    public String getSpeedlimit() {
        return speedLimit;
    }

    public void setSpeedlimit(String speedLimit) {
        this.speedLimit = speedLimit;
    }
    public boolean getError() {
        return error;
    }

    public void setError(boolean error) {
        this.error = error;
    }


}