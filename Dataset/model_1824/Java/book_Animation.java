





import java.util.List;
import java.util.ArrayList;

public class book_Animation extends Action {

    private int repeat;
    private float duration;
    private float delay;
    private boolean autoReverse;





    private book_ImageFlash book_imageflash;




    private book_ImageFlash book_imageflash;


    public book_Animation(
        int repeat,        float duration,        float delay,        boolean autoReverse    ) {
        super(
        );
        this.repeat = repeat;
        this.duration = duration;
        this.delay = delay;
        this.autoReverse = autoReverse;
    }


    public int getRepeat() {
        return repeat;
    }

    public void setRepeat(int repeat) {
        this.repeat = repeat;
    }
    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
    }
    public float getDelay() {
        return delay;
    }

    public void setDelay(float delay) {
        this.delay = delay;
    }
    public boolean getAutoreverse() {
        return autoReverse;
    }

    public void setAutoreverse(boolean autoReverse) {
        this.autoReverse = autoReverse;
    }

    public book_ImageFlash getBook_imageflash() {
        return book_imageflash;
    }

    public void setBook_imageflash(book_ImageFlash book_imageflash) {
        this.book_imageflash = book_imageflash;
    }
    public book_ImageFlash getBook_imageflash() {
        return book_imageflash;
    }

    public void setBook_imageflash(book_ImageFlash book_imageflash) {
        this.book_imageflash = book_imageflash;
    }

}