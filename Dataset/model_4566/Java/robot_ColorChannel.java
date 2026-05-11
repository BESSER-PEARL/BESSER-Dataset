





import java.util.List;
import java.util.ArrayList;

public class robot_ColorChannel extends Channel {

    private String mode;



    public robot_ColorChannel(
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