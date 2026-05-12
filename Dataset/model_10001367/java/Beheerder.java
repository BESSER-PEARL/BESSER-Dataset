





import java.util.List;
import java.util.ArrayList;

public class Beheerder  {

    private boolean rechten;



    public Beheerder(
        boolean rechten    ) {
        this.rechten = rechten;
    }


    public boolean getRechten() {
        return rechten;
    }

    public void setRechten(boolean rechten) {
        this.rechten = rechten;
    }


}