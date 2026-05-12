





import java.util.List;
import java.util.ArrayList;

public class connection_XmlFileConnection extends Connection {

    private boolean Guess;
    private String XmlFilePath;
    private String XsdFilePath;
    private String Encoding;
    private String MaskXPattern;



    public connection_XmlFileConnection(
        boolean Guess,        String XmlFilePath,        String XsdFilePath,        String Encoding,        String MaskXPattern    ) {
        super(
        );
        this.Guess = Guess;
        this.XmlFilePath = XmlFilePath;
        this.XsdFilePath = XsdFilePath;
        this.Encoding = Encoding;
        this.MaskXPattern = MaskXPattern;
    }


    public boolean getGuess() {
        return Guess;
    }

    public void setGuess(boolean Guess) {
        this.Guess = Guess;
    }
    public String getXmlfilepath() {
        return XmlFilePath;
    }

    public void setXmlfilepath(String XmlFilePath) {
        this.XmlFilePath = XmlFilePath;
    }
    public String getXsdfilepath() {
        return XsdFilePath;
    }

    public void setXsdfilepath(String XsdFilePath) {
        this.XsdFilePath = XsdFilePath;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
    }
    public String getMaskxpattern() {
        return MaskXPattern;
    }

    public void setMaskxpattern(String MaskXPattern) {
        this.MaskXPattern = MaskXPattern;
    }


}