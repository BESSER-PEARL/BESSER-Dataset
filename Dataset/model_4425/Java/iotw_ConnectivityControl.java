





import java.util.List;
import java.util.ArrayList;

public class iotw_ConnectivityControl extends Control {

    private String constraints;



    public iotw_ConnectivityControl(
        String constraints    ) {
        super(
        );
        this.constraints = constraints;
    }


    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }


}