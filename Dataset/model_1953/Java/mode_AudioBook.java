





import java.util.List;
import java.util.ArrayList;

public class mode_AudioBook extends MediaArtifact {

    private int length;



    public mode_AudioBook(
        int length    ) {
        super(
        );
        this.length = length;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}