





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_DurationArtifact extends Artifact {

    private int duration;



    public MediaLibrary_DurationArtifact(
        int duration    ) {
        super(
        );
        this.duration = duration;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}