





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwPackage_HwPackagePin extends HwEndPoint {

    private String pinNo;
    private String altNames;



    public MARTE_HwPackage_HwPackagePin(
        String pinNo,        String altNames    ) {
        super(
        );
        this.pinNo = pinNo;
        this.altNames = altNames;
    }


    public String getPinno() {
        return pinNo;
    }

    public void setPinno(String pinNo) {
        this.pinNo = pinNo;
    }
    public String getAltnames() {
        return altNames;
    }

    public void setAltnames(String altNames) {
        this.altNames = altNames;
    }


}