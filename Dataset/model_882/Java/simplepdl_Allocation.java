





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Allocation extends ProcessElement {

    private int count;



    public simplepdl_Allocation(
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