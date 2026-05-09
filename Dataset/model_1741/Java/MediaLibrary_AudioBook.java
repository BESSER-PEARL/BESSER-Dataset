





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_AudioBook extends DurationArtifact {

    private int currentPosition;



    public MediaLibrary_AudioBook(
        int currentPosition    ) {
        super(
        );
        this.currentPosition = currentPosition;
    }


    public int getCurrentposition() {
        return currentPosition;
    }

    public void setCurrentposition(int currentPosition) {
        this.currentPosition = currentPosition;
    }


}