





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_EReader extends Device {

    private String audioEnabled;
    private String videoEnabled;



    public MediaLibrary_EReader(
        String audioEnabled,        String videoEnabled    ) {
        super(
        );
        this.audioEnabled = audioEnabled;
        this.videoEnabled = videoEnabled;
    }


    public String getAudioenabled() {
        return audioEnabled;
    }

    public void setAudioenabled(String audioEnabled) {
        this.audioEnabled = audioEnabled;
    }
    public String getVideoenabled() {
        return videoEnabled;
    }

    public void setVideoenabled(String videoEnabled) {
        this.videoEnabled = videoEnabled;
    }


}