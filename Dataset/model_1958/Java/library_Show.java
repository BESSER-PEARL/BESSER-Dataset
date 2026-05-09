





import java.util.List;
import java.util.ArrayList;

public class library_Show extends Command {

    private String what;



    public library_Show(
        String what    ) {
        super(
        );
        this.what = what;
    }


    public String getWhat() {
        return what;
    }

    public void setWhat(String what) {
        this.what = what;
    }


}