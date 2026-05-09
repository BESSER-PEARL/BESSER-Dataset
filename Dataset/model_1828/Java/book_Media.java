





import java.util.List;
import java.util.ArrayList;

public class book_Media extends Control {

    private int repeat;
    private boolean autoPlay;
    private int duration;
    private String url;



    public book_Media(
        int repeat,        boolean autoPlay,        int duration,        String url    ) {
        super(
        );
        this.repeat = repeat;
        this.autoPlay = autoPlay;
        this.duration = duration;
        this.url = url;
    }


    public int getRepeat() {
        return repeat;
    }

    public void setRepeat(int repeat) {
        this.repeat = repeat;
    }
    public boolean getAutoplay() {
        return autoPlay;
    }

    public void setAutoplay(boolean autoPlay) {
        this.autoPlay = autoPlay;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}