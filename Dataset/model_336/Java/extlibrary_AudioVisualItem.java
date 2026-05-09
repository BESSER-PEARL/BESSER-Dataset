





import java.util.List;
import java.util.ArrayList;

public class extlibrary_AudioVisualItem extends _15LbQG60EeGkd4g88tZXfA {

    private int minutesLength;
    private boolean damaged;
    private String title;



    public extlibrary_AudioVisualItem(
        int minutesLength,        boolean damaged,        String title    ) {
        super(
        );
        this.minutesLength = minutesLength;
        this.damaged = damaged;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}