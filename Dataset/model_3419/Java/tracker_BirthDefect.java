





import java.util.List;
import java.util.ArrayList;

public class tracker_BirthDefect extends Event {

    private boolean freemartin;



    public tracker_BirthDefect(
        boolean freemartin    ) {
        super(
        );
        this.freemartin = freemartin;
    }


    public boolean getFreemartin() {
        return freemartin;
    }

    public void setFreemartin(boolean freemartin) {
        this.freemartin = freemartin;
    }


}