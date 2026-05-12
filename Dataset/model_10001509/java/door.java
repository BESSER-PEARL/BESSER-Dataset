





import java.util.List;
import java.util.ArrayList;

public class door  {

    private boolean close;





    private elevator elevator;


    public door(
        boolean close    ) {
        this.close = close;
    }


    public boolean getClose() {
        return close;
    }

    public void setClose(boolean close) {
        this.close = close;
    }

    public elevator getElevator() {
        return elevator;
    }

    public void setElevator(elevator elevator) {
        this.elevator = elevator;
    }

}