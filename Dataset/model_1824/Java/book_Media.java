





import java.util.List;
import java.util.ArrayList;

public class book_Media extends Control {

    private boolean autoPlay;
    private int repeat;
    private int duration;
    private String url;



    public book_Media(
        boolean autoPlay,        int repeat,        int duration,        String url    ) {
        super(
        );
        this.autoPlay = autoPlay;
        this.repeat = repeat;
        this.duration = duration;
        this.url = url;
    }


    public boolean getAutoplay() {
        return autoPlay;
    }

    public void setAutoplay(boolean autoPlay) {
        this.autoPlay = autoPlay;
    }
    public int getRepeat() {
        return repeat;
    }

    public void setRepeat(int repeat) {
        this.repeat = repeat;
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