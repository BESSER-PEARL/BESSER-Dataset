





import java.util.List;
import java.util.ArrayList;

public class book_ImageFlash extends Control {

    private int duration;
    private String images;



    public book_ImageFlash(
        int duration,        String images    ) {
        super(
        );
        this.duration = duration;
        this.images = images;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getImages() {
        return images;
    }

    public void setImages(String images) {
        this.images = images;
    }


}