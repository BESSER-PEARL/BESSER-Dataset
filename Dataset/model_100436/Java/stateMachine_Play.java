





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Play extends IvrAction {

    private String baseURL;
    private String mediaURI;



    public stateMachine_Play(
        String baseURL,        String mediaURI    ) {
        super(
        );
        this.baseURL = baseURL;
        this.mediaURI = mediaURI;
    }


    public String getBaseurl() {
        return baseURL;
    }

    public void setBaseurl(String baseURL) {
        this.baseURL = baseURL;
    }
    public String getMediauri() {
        return mediaURI;
    }

    public void setMediauri(String mediaURI) {
        this.mediaURI = mediaURI;
    }


}