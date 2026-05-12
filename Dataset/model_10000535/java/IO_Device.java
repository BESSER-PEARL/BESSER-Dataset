





import java.util.List;
import java.util.ArrayList;

public class IO_Device  {

    private int counter;





    private Operating_System operating_system;


    public IO_Device(
        int counter    ) {
        this.counter = counter;
    }


    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}