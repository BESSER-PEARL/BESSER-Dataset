





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_FontEntry extends IdentifiedElt {

    private String weight;
    private String charSet;
    private String pitchAndFamily;
    private String attributes;
    private String unicode;
    private String name;





    private FontsTable fontstable;


    public DatadiagramMLTextFormat_FontEntry(
        String weight,        String charSet,        String pitchAndFamily,        String attributes,        String unicode,        String name    ) {
        super(
        );
        this.weight = weight;
        this.charSet = charSet;
        this.pitchAndFamily = pitchAndFamily;
        this.attributes = attributes;
        this.unicode = unicode;
        this.name = name;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getCharset() {
        return charSet;
    }

    public void setCharset(String charSet) {
        this.charSet = charSet;
    }
    public String getPitchandfamily() {
        return pitchAndFamily;
    }

    public void setPitchandfamily(String pitchAndFamily) {
        this.pitchAndFamily = pitchAndFamily;
    }
    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }
    public String getUnicode() {
        return unicode;
    }

    public void setUnicode(String unicode) {
        this.unicode = unicode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FontsTable getFontstable() {
        return fontstable;
    }

    public void setFontstable(FontsTable fontstable) {
        this.fontstable = fontstable;
    }

}