





import java.util.List;
import java.util.ArrayList;

public class extlibrary_AudioVisualItem extends _15LbQG60EeGkd4g88tZXfA {

    private String title;
    private boolean damaged;
    private int length;



    public extlibrary_AudioVisualItem(
        String title,        boolean damaged,        int length    ) {
        super(
        );
        this.title = title;
        this.damaged = damaged;
        this.length = length;
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
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}