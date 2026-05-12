





import java.util.List;
import java.util.ArrayList;

public class model_Call  {

    private None LOGGER;
    private int MAX;
    private int MIN;
    private int number;



    public model_Call(
        None LOGGER,        int MAX,        int MIN,        int number    ) {
        this.LOGGER = LOGGER;
        this.MAX = MAX;
        this.MIN = MIN;
        this.number = number;
    }


    public None getLogger() {
        return LOGGER;
    }

    public void setLogger(None LOGGER) {
        this.LOGGER = LOGGER;
    }
    public int getMax() {
        return MAX;
    }

    public void setMax(int MAX) {
        this.MAX = MAX;
    }
    public int getMin() {
        return MIN;
    }

    public void setMin(int MIN) {
        this.MIN = MIN;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}