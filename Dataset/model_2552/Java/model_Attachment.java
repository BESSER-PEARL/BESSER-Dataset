





import java.util.List;
import java.util.ArrayList;

public class model_Attachment extends BasicObject {

    private String objectId;
    private String data;
    private String key;



    public model_Attachment(
        String objectId,        String data,        String key    ) {
        super(
        );
        this.objectId = objectId;
        this.data = data;
        this.key = key;
    }


    public String getObjectid() {
        return objectId;
    }

    public void setObjectid(String objectId) {
        this.objectId = objectId;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}