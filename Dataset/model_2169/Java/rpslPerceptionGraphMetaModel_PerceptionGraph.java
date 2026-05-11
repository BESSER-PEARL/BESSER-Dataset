





import java.util.List;
import java.util.ArrayList;

public class rpslPerceptionGraphMetaModel_PerceptionGraph  {

    private String doc;
    private String name;
    private String uuid;



    public rpslPerceptionGraphMetaModel_PerceptionGraph(
        String doc,        String name,        String uuid    ) {
        this.doc = doc;
        this.name = name;
        this.uuid = uuid;
    }


    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }


}