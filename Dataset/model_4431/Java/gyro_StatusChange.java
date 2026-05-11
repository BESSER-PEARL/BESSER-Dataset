





import java.util.List;
import java.util.ArrayList;

public class gyro_StatusChange extends Behavior {

    private String changeFailure;
    private String changeSuccess;
    private String changeRunning;



    public gyro_StatusChange(
        String changeFailure,        String changeSuccess,        String changeRunning    ) {
        super(
        );
        this.changeFailure = changeFailure;
        this.changeSuccess = changeSuccess;
        this.changeRunning = changeRunning;
    }


    public String getChangefailure() {
        return changeFailure;
    }

    public void setChangefailure(String changeFailure) {
        this.changeFailure = changeFailure;
    }
    public String getChangesuccess() {
        return changeSuccess;
    }

    public void setChangesuccess(String changeSuccess) {
        this.changeSuccess = changeSuccess;
    }
    public String getChangerunning() {
        return changeRunning;
    }

    public void setChangerunning(String changeRunning) {
        this.changeRunning = changeRunning;
    }


}