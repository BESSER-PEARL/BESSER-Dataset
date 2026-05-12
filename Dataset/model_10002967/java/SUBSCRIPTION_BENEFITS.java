





import java.util.List;
import java.util.ArrayList;

public class SUBSCRIPTION_BENEFITS  {

    private String key_name;
    private String _id;
    private String description;



    public SUBSCRIPTION_BENEFITS(
        String key_name,        String _id,        String description    ) {
        this.key_name = key_name;
        this._id = _id;
        this.description = description;
    }


    public String getKey_name() {
        return key_name;
    }

    public void setKey_name(String key_name) {
        this.key_name = key_name;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}