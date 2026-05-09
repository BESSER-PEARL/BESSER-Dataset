





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_Identifiable  {

    private String lastChange;
    private String desc;
    private String longName;
    private String identifier;



    public rif11a_ExchangeFile_Identifiable(
        String lastChange,        String desc,        String longName,        String identifier    ) {
        this.lastChange = lastChange;
        this.desc = desc;
        this.longName = longName;
        this.identifier = identifier;
    }


    public String getLastchange() {
        return lastChange;
    }

    public void setLastchange(String lastChange) {
        this.lastChange = lastChange;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
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


}