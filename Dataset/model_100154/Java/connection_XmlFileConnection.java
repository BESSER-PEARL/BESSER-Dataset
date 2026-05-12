





import java.util.List;
import java.util.ArrayList;

public class connection_XmlFileConnection extends Connection {

    private boolean Guess;
    private String Encoding;
    private String outputFilePath;
    private String XmlFilePath;
    private boolean inputModel;
    private String MaskXPattern;
    private String XsdFilePath;



    public connection_XmlFileConnection(
        boolean Guess,        String Encoding,        String outputFilePath,        String XmlFilePath,        boolean inputModel,        String MaskXPattern,        String XsdFilePath    ) {
        super(
        );
        this.Guess = Guess;
        this.Encoding = Encoding;
        this.outputFilePath = outputFilePath;
        this.XmlFilePath = XmlFilePath;
        this.inputModel = inputModel;
        this.MaskXPattern = MaskXPattern;
        this.XsdFilePath = XsdFilePath;
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
    public String getOutputfilepath() {
        return outputFilePath;
    }

    public void setOutputfilepath(String outputFilePath) {
        this.outputFilePath = outputFilePath;
    }
    public String getXmlfilepath() {
        return XmlFilePath;
    }

    public void setXmlfilepath(String XmlFilePath) {
        this.XmlFilePath = XmlFilePath;
    }
    public boolean getInputmodel() {
        return inputModel;
    }

    public void setInputmodel(boolean inputModel) {
        this.inputModel = inputModel;
    }
    public String getMaskxpattern() {
        return MaskXPattern;
    }

    public void setMaskxpattern(String MaskXPattern) {
        this.MaskXPattern = MaskXPattern;
    }
    public String getXsdfilepath() {
        return XsdFilePath;
    }

    public void setXsdfilepath(String XsdFilePath) {
        this.XsdFilePath = XsdFilePath;
    }


}