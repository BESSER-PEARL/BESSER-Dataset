





import java.util.List;
import java.util.ArrayList;

public class connection_HL7Connection extends FileConnection {

    private String StartChar;
    private String outputFilePath;
    private String EndChar;



    public connection_HL7Connection(
        String StartChar,        String outputFilePath,        String EndChar    ) {
        super(
        );
        this.StartChar = StartChar;
        this.outputFilePath = outputFilePath;
        this.EndChar = EndChar;
    }


    public String getStartchar() {
        return StartChar;
    }

    public void setStartchar(String StartChar) {
        this.StartChar = StartChar;
    }
    public String getOutputfilepath() {
        return outputFilePath;
    }

    public void setOutputfilepath(String outputFilePath) {
        this.outputFilePath = outputFilePath;
    }
    public String getEndchar() {
        return EndChar;
    }

    public void setEndchar(String EndChar) {
        this.EndChar = EndChar;
    }


}