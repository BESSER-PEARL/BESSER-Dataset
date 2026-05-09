





import java.util.List;
import java.util.ArrayList;

public class extlibrary_AudioVisualItem extends CirculatingItem {

    private String title;
    private int minutesLength;
    private boolean damaged;



    public extlibrary_AudioVisualItem(
        String title,        int minutesLength,        boolean damaged    ) {
        super(
        );
        this.title = title;
        this.minutesLength = minutesLength;
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
    public boolean getDamaged() {
        return damaged;
    }

    public void setDamaged(boolean damaged) {
        this.damaged = damaged;
    }


}