





import java.util.List;
import java.util.ArrayList;

public class fenix_Occupation  {

    private int current;
    private int max;





    private fenix_Shift fenix_shift;


    public fenix_Occupation(
        int current,        int max    ) {
        this.current = current;
        this.max = max;
    }


    public int getCurrent() {
        return current;
    }

    public void setCurrent(int current) {
        this.current = current;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public fenix_Shift getFenix_shift() {
        return fenix_shift;
    }

    public void setFenix_shift(fenix_Shift fenix_shift) {
        this.fenix_shift = fenix_shift;
    }

}