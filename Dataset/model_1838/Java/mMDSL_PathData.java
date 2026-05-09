





import java.util.List;
import java.util.ArrayList;

public class mMDSL_PathData  {

    private String closepath;





    private mMDSL_Path mmdsl_path;


    public mMDSL_PathData(
        String closepath    ) {
        this.closepath = closepath;
    }


    public String getClosepath() {
        return closepath;
    }

    public void setClosepath(String closepath) {
        this.closepath = closepath;
    }

    public mMDSL_Path getMmdsl_path() {
        return mmdsl_path;
    }

    public void setMmdsl_path(mMDSL_Path mmdsl_path) {
        this.mmdsl_path = mmdsl_path;
    }

}