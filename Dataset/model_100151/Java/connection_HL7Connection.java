





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String StartChar;
    private String EndChar;



    public connection_HL7Connection(
        String StartChar,        String EndChar    ) {
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
    public String getEndchar() {
        return EndChar;
    }

    public void setEndchar(String EndChar) {
        this.EndChar = EndChar;
    }


}