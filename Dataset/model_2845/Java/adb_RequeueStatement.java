





import java.util.List;
import java.util.ArrayList;

public class adb_RequeueStatement extends SimpleStatement {

    private boolean abort;





    private adb_Name adb_name;


    public adb_RequeueStatement(
        boolean abort    ) {
        super(
        );
        this.abort = abort;
    }


    public boolean getAbort() {
        return abort;
    }

    public void setAbort(boolean abort) {
        this.abort = abort;
    }

    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }

}