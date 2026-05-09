





import java.util.List;
import java.util.ArrayList;

public class library_AudioVisualItem extends CirculatingItem {

    private boolean damaged;
    private String title;
    private int minutesLength;



    public library_AudioVisualItem(
        boolean damaged,        String title,        int minutesLength    ) {
        super(
        );
        this.damaged = damaged;
        this.title = title;
        this.minutesLength = minutesLength;
    }


    public boolean getDamaged() {
        return damaged;
    }

    public void setDamaged(boolean damaged) {
        this.damaged = damaged;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getMinuteslength() {
        return minutesLength;
    }

    public void setMinuteslength(int minutesLength) {
        this.minutesLength = minutesLength;
    }


}