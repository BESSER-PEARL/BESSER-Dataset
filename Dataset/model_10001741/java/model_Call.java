





import java.util.List;
import java.util.ArrayList;

public class model_Call  {

    private int MIN;
    private int MAX;
    private None LOGGER;
    private int number;



    public model_Call(
        int MIN,        int MAX,        None LOGGER,        int number    ) {
        this.MIN = MIN;
        this.MAX = MAX;
        this.LOGGER = LOGGER;
        this.number = number;
    }


    public int getMin() {
        return MIN;
    }

    public void setMin(int MIN) {
        this.MIN = MIN;
    }
    public int getMax() {
        return MAX;
    }

    public void setMax(int MAX) {
        this.MAX = MAX;
    }
    public None getLogger() {
        return LOGGER;
    }

    public void setLogger(None LOGGER) {
        this.LOGGER = LOGGER;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}