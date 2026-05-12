





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String EndChar;
    private String outputFilePath;
    private String StartChar;



    public connection_HL7Connection(
        String EndChar,        String outputFilePath,        String StartChar    ) {
        super(
        );
        this.EndChar = EndChar;
        this.outputFilePath = outputFilePath;
        this.StartChar = StartChar;
    }


    public String getEndchar() {
        return EndChar;
    }

    public void setEndchar(String EndChar) {
        this.EndChar = EndChar;
    }
    public String getOutputfilepath() {
        return outputFilePath;
    }

    public void setOutputfilepath(String outputFilePath) {
        this.outputFilePath = outputFilePath;
    }
    public String getStartchar() {
        return StartChar;
    }

    public void setStartchar(String StartChar) {
        this.StartChar = StartChar;
    }


}