





import java.util.List;
import java.util.ArrayList;

public class miniJava_OutputStream  {

    private String stream;





    private miniJava_State minijava_state;


    public miniJava_OutputStream(
        String stream    ) {
        this.stream = stream;
    }


    public String getStream() {
        return stream;
    }

    public void setStream(String stream) {
        this.stream = stream;
    }

    public miniJava_State getMinijava_state() {
        return minijava_state;
    }

    public void setMinijava_state(miniJava_State minijava_state) {
        this.minijava_state = minijava_state;
    }

}