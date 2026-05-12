





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_FontEntry extends IdentifiedElt {

    private String charSet;
    private String name;
    private String weight;
    private String pitchAndFamily;
    private String unicode;
    private String attributes;





    private FontsTable fontstable;


    public DatadiagramMLXForm_FontEntry(
        String charSet,        String name,        String weight,        String pitchAndFamily,        String unicode,        String attributes    ) {
        super(
        );
        this.charSet = charSet;
        this.name = name;
        this.weight = weight;
        this.pitchAndFamily = pitchAndFamily;
        this.unicode = unicode;
        this.attributes = attributes;
    }


    public String getCharset() {
        return charSet;
    }

    public void setCharset(String charSet) {
        this.charSet = charSet;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getPitchandfamily() {
        return pitchAndFamily;
    }

    public void setPitchandfamily(String pitchAndFamily) {
        this.pitchAndFamily = pitchAndFamily;
    }
    public String getUnicode() {
        return unicode;
    }

    public void setUnicode(String unicode) {
        this.unicode = unicode;
    }
    public String getAttributes() {
        return attributes;
    }

    public void setAttributes(String attributes) {
        this.attributes = attributes;
    }

    public FontsTable getFontstable() {
        return fontstable;
    }

    public void setFontstable(FontsTable fontstable) {
        this.fontstable = fontstable;
    }

}