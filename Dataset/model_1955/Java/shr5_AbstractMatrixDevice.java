





import java.util.List;
import java.util.ArrayList;

public class shr5_AbstractMatrixDevice extends AbstraktGegenstand, MatrixDevice {

    private int deviceRating;



    public shr5_AbstractMatrixDevice(
        int deviceRating    ) {
        super(
        );
        this.deviceRating = deviceRating;
    }


    public int getDevicerating() {
        return deviceRating;
    }

    public void setDevicerating(int deviceRating) {
        this.deviceRating = deviceRating;
    }


}