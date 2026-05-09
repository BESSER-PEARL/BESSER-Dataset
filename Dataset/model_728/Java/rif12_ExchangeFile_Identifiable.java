





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_Identifiable  {

    private String longName;
    private String identifier;
    private String desc;
    private String lastChange;



    public rif12_ExchangeFile_Identifiable(
        String longName,        String identifier,        String desc,        String lastChange    ) {
        this.longName = longName;
        this.identifier = identifier;
        this.desc = desc;
        this.lastChange = lastChange;
    }


    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }
    public String getLastchange() {
        return lastChange;
    }

    public void setLastchange(String lastChange) {
        this.lastChange = lastChange;
    }


}