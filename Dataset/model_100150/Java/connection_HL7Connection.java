





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String EndChar;
    private String StartChar;



    public connection_HL7Connection(
        String EndChar,        String StartChar    ) {
        super(
        );
        this.EndChar = EndChar;
        this.StartChar = StartChar;
    }


    public String getEndchar() {
        return EndChar;
    }

    public void setEndchar(String EndChar) {
        this.EndChar = EndChar;
    }
    public String getStartchar() {
        return StartChar;
    }

    public void setStartchar(String StartChar) {
        this.StartChar = StartChar;
    }


}