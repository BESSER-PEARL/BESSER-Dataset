





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_FaceName extends IdentifiedElt {

    private String charSet;
    private String panos;
    private String name;
    private String unicodeRanges;
    private String flags;





    private FaceNamesTable facenamestable;


    public DatadiagramMLTextFormat_FaceName(
        String charSet,        String panos,        String name,        String unicodeRanges,        String flags    ) {
        super(
        );
        this.charSet = charSet;
        this.panos = panos;
        this.name = name;
        this.unicodeRanges = unicodeRanges;
        this.flags = flags;
    }


    public String getCharset() {
        return charSet;
    }

    public void setCharset(String charSet) {
        this.charSet = charSet;
    }
    public String getPanos() {
        return panos;
    }

    public void setPanos(String panos) {
        this.panos = panos;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnicoderanges() {
        return unicodeRanges;
    }

    public void setUnicoderanges(String unicodeRanges) {
        this.unicodeRanges = unicodeRanges;
    }
    public String getFlags() {
        return flags;
    }

    public void setFlags(String flags) {
        this.flags = flags;
    }

    public FaceNamesTable getFacenamestable() {
        return facenamestable;
    }

    public void setFacenamestable(FaceNamesTable facenamestable) {
        this.facenamestable = facenamestable;
    }

}