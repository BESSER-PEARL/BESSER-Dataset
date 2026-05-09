





import java.util.List;
import java.util.ArrayList;

public class extlibrary_AudioVisualItem extends _15LbQG60EeGkd4g88tZXfA {

    private int length;
    private boolean damaged;
    private String title;



    public extlibrary_AudioVisualItem(
        int length,        boolean damaged,        String title    ) {
        super(
        );
        this.length = length;
        this.damaged = damaged;
        this.title = title;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
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