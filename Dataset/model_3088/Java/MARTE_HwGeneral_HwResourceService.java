





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwGeneral_HwResourceService extends GrService {

    private String consumption;
    private String dissipation;



    public MARTE_HwGeneral_HwResourceService(
        String consumption,        String dissipation    ) {
        super(
        );
        this.consumption = consumption;
        this.dissipation = dissipation;
    }


    public String getConsumption() {
        return consumption;
    }

    public void setConsumption(String consumption) {
        this.consumption = consumption;
    }
    public String getDissipation() {
        return dissipation;
    }

    public void setDissipation(String dissipation) {
        this.dissipation = dissipation;
    }


}