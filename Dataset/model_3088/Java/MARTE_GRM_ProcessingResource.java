





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_ProcessingResource extends Resource {

    private String speedFactor;



    public MARTE_GRM_ProcessingResource(
        String speedFactor    ) {
        super(
        );
        this.speedFactor = speedFactor;
    }


    public String getSpeedfactor() {
        return speedFactor;
    }

    public void setSpeedfactor(String speedFactor) {
        this.speedFactor = speedFactor;
    }


}