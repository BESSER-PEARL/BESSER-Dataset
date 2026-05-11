





import java.util.List;
import java.util.ArrayList;

public class pcm_av_resourcetype_av_ResourceSignature extends Entity {

    private int resourceServiceId;





    private ResourceInterface resourceinterface;


    public pcm_av_resourcetype_av_ResourceSignature(
        int resourceServiceId    ) {
        super(
        );
        this.resourceServiceId = resourceServiceId;
    }


    public int getResourceserviceid() {
        return resourceServiceId;
    }

    public void setResourceserviceid(int resourceServiceId) {
        this.resourceServiceId = resourceServiceId;
    }

    public ResourceInterface getResourceinterface() {
        return resourceinterface;
    }

    public void setResourceinterface(ResourceInterface resourceinterface) {
        this.resourceinterface = resourceinterface;
    }

}