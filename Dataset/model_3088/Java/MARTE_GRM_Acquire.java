





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_Acquire extends GrService {

    private String isBlocking;



    public MARTE_GRM_Acquire(
        String isBlocking    ) {
        super(
        );
        this.isBlocking = isBlocking;
    }


    public String getIsblocking() {
        return isBlocking;
    }

    public void setIsblocking(String isBlocking) {
        this.isBlocking = isBlocking;
    }


}