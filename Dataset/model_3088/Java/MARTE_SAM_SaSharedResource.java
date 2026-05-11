





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaSharedResource extends MutualExclusionResource {

    private String acquisT;
    private String capacity;
    private String isConsum;
    private String releaseT;
    private String isPreemp;



    public MARTE_SAM_SaSharedResource(
        String acquisT,        String capacity,        String isConsum,        String releaseT,        String isPreemp    ) {
        super(
        );
        this.acquisT = acquisT;
        this.capacity = capacity;
        this.isConsum = isConsum;
        this.releaseT = releaseT;
        this.isPreemp = isPreemp;
    }


    public String getAcquist() {
        return acquisT;
    }

    public void setAcquist(String acquisT) {
        this.acquisT = acquisT;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public String getIsconsum() {
        return isConsum;
    }

    public void setIsconsum(String isConsum) {
        this.isConsum = isConsum;
    }
    public String getReleaset() {
        return releaseT;
    }

    public void setReleaset(String releaseT) {
        this.releaseT = releaseT;
    }
    public String getIspreemp() {
        return isPreemp;
    }

    public void setIspreemp(String isPreemp) {
        this.isPreemp = isPreemp;
    }


}