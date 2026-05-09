





import java.util.List;
import java.util.ArrayList;

public class library_AudioVisualItem extends CirculatingItem {

    private String title;
    private boolean damaged;
    private int minutesLength;



    public library_AudioVisualItem(
        String title,        boolean damaged,        int minutesLength    ) {
        super(
        );
        this.title = title;
        this.damaged = damaged;
        this.minutesLength = minutesLength;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getDamaged() {
        return damaged;
    }

    public void setDamaged(boolean damaged) {
        this.damaged = damaged;
    }
    public int getMinuteslength() {
        return minutesLength;
    }

    public void setMinuteslength(int minutesLength) {
        this.minutesLength = minutesLength;
    }


}