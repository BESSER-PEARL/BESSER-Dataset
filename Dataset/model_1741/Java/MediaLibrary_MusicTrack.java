





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_MusicTrack extends DurationArtifact {

    private String label;



    public MediaLibrary_MusicTrack(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}