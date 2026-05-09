





import java.util.List;
import java.util.ArrayList;

public class MediaPlayer_Playlist extends BaseObject {

    private boolean repeat;
    private String name;



    public MediaPlayer_Playlist(
        boolean repeat,        String name    ) {
        super(
        );
        this.repeat = repeat;
        this.name = name;
    }


    public boolean getRepeat() {
        return repeat;
    }

    public void setRepeat(boolean repeat) {
        this.repeat = repeat;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}