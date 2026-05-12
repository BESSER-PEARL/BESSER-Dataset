





import java.util.List;
import java.util.ArrayList;

public class connection_XmlFileConnection extends Connection {

    private String XsdFilePath;
    private String XmlFilePath;
    private boolean Guess;
    private String Encoding;
    private String MaskXPattern;



    public connection_XmlFileConnection(
        String XsdFilePath,        String XmlFilePath,        boolean Guess,        String Encoding,        String MaskXPattern    ) {
        super(
        );
        this.XsdFilePath = XsdFilePath;
        this.XmlFilePath = XmlFilePath;
        this.Guess = Guess;
        this.Encoding = Encoding;
        this.MaskXPattern = MaskXPattern;
    }


    public String getXsdfilepath() {
        return XsdFilePath;
    }

    public void setXsdfilepath(String XsdFilePath) {
        this.XsdFilePath = XsdFilePath;
    }
    public String getXmlfilepath() {
        return XmlFilePath;
    }

    public void setXmlfilepath(String XmlFilePath) {
        this.XmlFilePath = XmlFilePath;
    }
    public boolean getGuess() {
        return Guess;
    }

    public void setGuess(boolean Guess) {
        this.Guess = Guess;
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