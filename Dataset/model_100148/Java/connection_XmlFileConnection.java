





import java.util.List;
import java.util.ArrayList;

public class connection_XmlFileConnection extends Connection {

    private String MaskXPattern;
    private boolean inputModel;
    private String fileContent;
    private String Encoding;
    private String XmlFilePath;
    private String XsdFilePath;
    private String outputFilePath;
    private boolean Guess;



    public connection_XmlFileConnection(
        String MaskXPattern,        boolean inputModel,        String fileContent,        String Encoding,        String XmlFilePath,        String XsdFilePath,        String outputFilePath,        boolean Guess    ) {
        super(
        );
        this.MaskXPattern = MaskXPattern;
        this.inputModel = inputModel;
        this.fileContent = fileContent;
        this.Encoding = Encoding;
        this.XmlFilePath = XmlFilePath;
        this.XsdFilePath = XsdFilePath;
        this.outputFilePath = outputFilePath;
        this.Guess = Guess;
    }


    public String getMaskxpattern() {
        return MaskXPattern;
    }

    public void setMaskxpattern(String MaskXPattern) {
        this.MaskXPattern = MaskXPattern;
    }
    public boolean getInputmodel() {
        return inputModel;
    }

    public void setInputmodel(boolean inputModel) {
        this.inputModel = inputModel;
    }
    public String getFilecontent() {
        return fileContent;
    }

    public void setFilecontent(String fileContent) {
        this.fileContent = fileContent;
    }
    public String getEncoding() {
        return Encoding;
    }

    public void setEncoding(String Encoding) {
        this.Encoding = Encoding;
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
    public String getOutputfilepath() {
        return outputFilePath;
    }

    public void setOutputfilepath(String outputFilePath) {
        this.outputFilePath = outputFilePath;
    }
    public boolean getGuess() {
        return Guess;
    }

    public void setGuess(boolean Guess) {
        this.Guess = Guess;
    }


}