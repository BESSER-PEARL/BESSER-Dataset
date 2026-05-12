





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String StartChar;
    private int EndChar;



    public connection_HL7Connection(
        String StartChar,        int EndChar    ) {
        super(
        );
        this.StartChar = StartChar;
        this.EndChar = EndChar;
    }


    public String getStartchar() {
        return StartChar;
    }

    public void setStartchar(String StartChar) {
        this.StartChar = StartChar;
    }
    public int getEndchar() {
        return EndChar;
    }

    public void setEndchar(int EndChar) {
        this.EndChar = EndChar;
    }


}