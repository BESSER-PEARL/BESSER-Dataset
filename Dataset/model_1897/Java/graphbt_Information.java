





import java.util.List;
import java.util.ArrayList;

public class graphbt_Information  {

    private String key;
    private String value;





    private graphbt_MapInformation graphbt_mapinformation;


    public graphbt_Information(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public graphbt_MapInformation getGraphbt_mapinformation() {
        return graphbt_mapinformation;
    }

    public void setGraphbt_mapinformation(graphbt_MapInformation graphbt_mapinformation) {
        this.graphbt_mapinformation = graphbt_mapinformation;
    }

}