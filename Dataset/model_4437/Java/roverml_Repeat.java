





import java.util.List;
import java.util.ArrayList;

public class roverml_Repeat extends Block, Command {

    private int count;



    public roverml_Repeat(
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