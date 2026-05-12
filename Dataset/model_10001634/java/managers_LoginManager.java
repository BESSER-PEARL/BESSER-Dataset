





import java.util.List;
import java.util.ArrayList;

public class managers_LoginManager  {

    private None in;
    private None out;
    private String inputLine;



    public managers_LoginManager(
        None in,        None out,        String inputLine    ) {
        this.in = in;
        this.out = out;
        this.inputLine = inputLine;
    }


    public None getIn() {
        return in;
    }

    public void setIn(None in) {
        this.in = in;
    }
    public None getOut() {
        return out;
    }

    public void setOut(None out) {
        this.out = out;
    }
    public String getInputline() {
        return inputLine;
    }

    public void setInputline(String inputLine) {
        this.inputLine = inputLine;
    }


}