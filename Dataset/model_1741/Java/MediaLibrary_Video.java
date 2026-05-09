





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Video extends DurationArtifact {

    private String fps;



    public MediaLibrary_Video(
        String fps    ) {
        super(
        );
        this.fps = fps;
    }


    public String getFps() {
        return fps;
    }

    public void setFps(String fps) {
        this.fps = fps;
    }


}