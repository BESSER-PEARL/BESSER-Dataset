





import java.util.List;
import java.util.ArrayList;

public class adb_DelayAlternative extends SelectAlternative {






    private adb_TimedEntryCall adb_timedentrycall;




    private adb_DelayStatement adb_delaystatement;


    public adb_DelayAlternative(
    ) {
        super(
        );
    }



    public adb_TimedEntryCall getAdb_timedentrycall() {
        return adb_timedentrycall;
    }

    public void setAdb_timedentrycall(adb_TimedEntryCall adb_timedentrycall) {
        this.adb_timedentrycall = adb_timedentrycall;
    }
    public adb_DelayStatement getAdb_delaystatement() {
        return adb_delaystatement;
    }

    public void setAdb_delaystatement(adb_DelayStatement adb_delaystatement) {
        this.adb_delaystatement = adb_delaystatement;
    }

}