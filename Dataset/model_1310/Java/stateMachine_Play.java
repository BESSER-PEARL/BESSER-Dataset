





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Play extends IvrAction {

    private String mediaURI;
    private String baseURL;



    public stateMachine_Play(
        String mediaURI,        String baseURL    ) {
        super(
        );
        this.mediaURI = mediaURI;
        this.baseURL = baseURL;
    }


    public String getMediauri() {
        return mediaURI;
    }

    public void setMediauri(String mediaURI) {
        this.mediaURI = mediaURI;
    }
    public String getBaseurl() {
        return baseURL;
    }

    public void setBaseurl(String baseURL) {
        this.baseURL = baseURL;
    }


}