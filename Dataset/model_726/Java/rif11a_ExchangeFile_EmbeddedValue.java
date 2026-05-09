





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_EmbeddedValue  {

    private String otherContent;
    private String key;



    public rif11a_ExchangeFile_EmbeddedValue(
        String otherContent,        String key    ) {
        this.otherContent = otherContent;
        this.key = key;
    }


    public String getOthercontent() {
        return otherContent;
    }

    public void setOthercontent(String otherContent) {
        this.otherContent = otherContent;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}