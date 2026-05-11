





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_SchedulableResource extends Resource {

    private String schedParams;



    public MARTE_GRM_SchedulableResource(
        String schedParams    ) {
        super(
        );
        this.schedParams = schedParams;
    }


    public String getSchedparams() {
        return schedParams;
    }

    public void setSchedparams(String schedParams) {
        this.schedParams = schedParams;
    }


}