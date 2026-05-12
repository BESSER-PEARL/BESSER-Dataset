





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLStyles_NamedRange  {

    private String name;
    private String hidden;
    private String refersTo;





    private NamesType namestype;


    public SpreadsheetMLStyles_NamedRange(
        String name,        String hidden,        String refersTo    ) {
        this.name = name;
        this.hidden = hidden;
        this.refersTo = refersTo;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHidden() {
        return hidden;
    }

    public void setHidden(String hidden) {
        this.hidden = hidden;
    }
    public String getRefersto() {
        return refersTo;
    }

    public void setRefersto(String refersTo) {
        this.refersTo = refersTo;
    }

    public NamesType getNamestype() {
        return namestype;
    }

    public void setNamestype(NamesType namestype) {
        this.namestype = namestype;
    }

}