





import java.util.List;
import java.util.ArrayList;

public class sadl_LiteralValue  {

    private String literalString;
    private String literalBoolean;
    private String literalNumber;





    private sadl_LiteralList sadl_literallist;


    public sadl_LiteralValue(
        String literalString,        String literalBoolean,        String literalNumber    ) {
        this.literalString = literalString;
        this.literalBoolean = literalBoolean;
        this.literalNumber = literalNumber;
    }


    public String getLiteralstring() {
        return literalString;
    }

    public void setLiteralstring(String literalString) {
        this.literalString = literalString;
    }
    public String getLiteralboolean() {
        return literalBoolean;
    }

    public void setLiteralboolean(String literalBoolean) {
        this.literalBoolean = literalBoolean;
    }
    public String getLiteralnumber() {
        return literalNumber;
    }

    public void setLiteralnumber(String literalNumber) {
        this.literalNumber = literalNumber;
    }

    public sadl_LiteralList getSadl_literallist() {
        return sadl_literallist;
    }

    public void setSadl_literallist(sadl_LiteralList sadl_literallist) {
        this.sadl_literallist = sadl_literallist;
    }

}