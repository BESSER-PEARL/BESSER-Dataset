





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_Identifiable  {

    private String identifier;
    private String desc;
    private String lastChange;
    private String longName;



    public rif12_ExchangeFile_Identifiable(
        String identifier,        String desc,        String lastChange,        String longName    ) {
        this.identifier = identifier;
        this.desc = desc;
        this.lastChange = lastChange;
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
    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
    }


}