





import java.util.List;
import java.util.ArrayList;

public class library_Manuscript extends Book {

    private int state;



    public library_Manuscript(
        int state    ) {
        super(
        );
        this.state = state;
    }


    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }


}