





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_EmbeddedValue  {

    private String key;
    private String otherContent;



    public rif11a_ExchangeFile_EmbeddedValue(
        String key,        String otherContent    ) {
        this.key = key;
        this.otherContent = otherContent;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getOthercontent() {
        return otherContent;
    }

    public void setOthercontent(String otherContent) {
        this.otherContent = otherContent;
    }


}