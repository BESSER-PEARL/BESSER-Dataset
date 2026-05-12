





import java.util.List;
import java.util.ArrayList;

public class BasePlayer  {

    private boolean isBusted;



    public BasePlayer(
        boolean isBusted    ) {
        this.isBusted = isBusted;
    }


    public boolean getIsbusted() {
        return isBusted;
    }

    public void setIsbusted(boolean isBusted) {
        this.isBusted = isBusted;
    }


}