





import java.util.List;
import java.util.ArrayList;

public class rover_Repeat extends Command {

    private int count;



    public rover_Repeat(
        int count    ) {
        super(
        );
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }


}