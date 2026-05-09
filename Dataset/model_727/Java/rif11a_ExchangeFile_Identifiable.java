





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_Identifiable  {

    private String longName;
    private String lastChange;
    private String desc;
    private String identifier;



    public rif11a_ExchangeFile_Identifiable(
        String longName,        String lastChange,        String desc,        String identifier    ) {
        this.longName = longName;
        this.lastChange = lastChange;
        this.desc = desc;
        this.identifier = identifier;
    }


    public String getLongname() {
        return longName;
    }

    public void setLongname(String longName) {
        this.longName = longName;
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
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}