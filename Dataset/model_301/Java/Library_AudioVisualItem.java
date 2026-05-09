





import java.util.List;
import java.util.ArrayList;

public class Library_AudioVisualItem extends CirculatingItem {

    private int minutesLength;
    private String title;
    private boolean damaged;



    public Library_AudioVisualItem(
        int minutesLength,        String title,        boolean damaged    ) {
        super(
        );
        this.minutesLength = minutesLength;
        this.title = title;
        this.damaged = damaged;
    }


    public int getMinuteslength() {
        return minutesLength;
    }

    public void setMinuteslength(int minutesLength) {
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


}