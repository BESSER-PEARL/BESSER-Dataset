





import java.util.List;
import java.util.ArrayList;

public class robot_LinearChannel extends Channel {

    private String mode;



    public robot_LinearChannel(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}