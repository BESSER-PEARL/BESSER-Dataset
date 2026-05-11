





import java.util.List;
import java.util.ArrayList;

public class gyro_Bumpers extends Condition {

    private String bumperKind;



    public gyro_Bumpers(
        String bumperKind    ) {
        super(
        );
        this.bumperKind = bumperKind;
    }


    public String getBumperkind() {
        return bumperKind;
    }

    public void setBumperkind(String bumperKind) {
        this.bumperKind = bumperKind;
    }


}