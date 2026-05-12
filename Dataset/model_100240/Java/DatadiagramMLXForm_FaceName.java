





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_FaceName extends IdentifiedElt {

    private String charSet;
    private String flags;
    private String unicodeRanges;
    private String panos;
    private String name;





    private FaceNamesTable facenamestable;


    public DatadiagramMLXForm_FaceName(
        String charSet,        String flags,        String unicodeRanges,        String panos,        String name    ) {
        super(
        );
        this.charSet = charSet;
        this.flags = flags;
        this.unicodeRanges = unicodeRanges;
        this.panos = panos;
        this.name = name;
    }


    public String getCharset() {
        return charSet;
    }

    public void setCharset(String charSet) {
        this.charSet = charSet;
    }
    public String getFlags() {
        return flags;
    }

    public void setFlags(String flags) {
        this.flags = flags;
    }
    public String getUnicoderanges() {
        return unicodeRanges;
    }

    public void setUnicoderanges(String unicodeRanges) {
        this.unicodeRanges = unicodeRanges;
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

    public FaceNamesTable getFacenamestable() {
        return facenamestable;
    }

    public void setFacenamestable(FaceNamesTable facenamestable) {
        this.facenamestable = facenamestable;
    }

}