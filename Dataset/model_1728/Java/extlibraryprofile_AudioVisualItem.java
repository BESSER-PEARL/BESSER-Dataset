





import java.util.List;
import java.util.ArrayList;

public class extlibraryprofile_AudioVisualItem extends CirculatingItem {

    private String minutesLength;
    private String damaged;



    public extlibraryprofile_AudioVisualItem(
        String minutesLength,        String damaged    ) {
        super(
        );
        this.minutesLength = minutesLength;
        this.damaged = damaged;
    }


    public String getMinuteslength() {
        return minutesLength;
    }

    public void setMinuteslength(String minutesLength) {
        this.minutesLength = minutesLength;
    }
    public String getDamaged() {
        return damaged;
    }

    public void setDamaged(String damaged) {
        this.damaged = damaged;
    }


}