





import java.util.List;
import java.util.ArrayList;

public class book_Animation extends Action {

    private int repeat;
    private boolean autoReverse;
    private float delay;
    private float duration;





    private book_ImageFlash book_imageflash;




    private book_ImageFlash book_imageflash;


    public book_Animation(
        int repeat,        boolean autoReverse,        float delay,        float duration    ) {
        super(
        );
        this.repeat = repeat;
        this.autoReverse = autoReverse;
        this.delay = delay;
        this.duration = duration;
    }


    public int getRepeat() {
        return repeat;
    }

    public void setRepeat(int repeat) {
        this.repeat = repeat;
    }
    public boolean getAutoreverse() {
        return autoReverse;
    }

    public void setAutoreverse(boolean autoReverse) {
        this.autoReverse = autoReverse;
    }
    public float getDelay() {
        return delay;
    }

    public void setDelay(float delay) {
        this.delay = delay;
    }
    public float getDuration() {
        return duration;
    }

    public void setDuration(float duration) {
        this.duration = duration;
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