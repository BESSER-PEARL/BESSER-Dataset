





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String outputFilePath;
    private String StartChar;
    private String EndChar;



    public connection_HL7Connection(
        String outputFilePath,        String StartChar,        String EndChar    ) {
        super(
        );
        this.outputFilePath = outputFilePath;
        this.StartChar = StartChar;
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
    public String getEndchar() {
        return EndChar;
    }

    public void setEndchar(String EndChar) {
        this.EndChar = EndChar;
    }


}