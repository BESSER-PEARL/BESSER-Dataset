





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Concurrency_EntryPoint extends Allocate {

    private String isReentrant;



    public MARTE_SW_Concurrency_EntryPoint(
        String isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
    }


    public String getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(String isReentrant) {
        this.isReentrant = isReentrant;
    }


}