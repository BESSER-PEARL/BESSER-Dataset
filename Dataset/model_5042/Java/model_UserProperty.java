





import java.util.List;
import java.util.ArrayList;

public class model_UserProperty extends IEntity {

    private String global_;
    private String user;
    private String default;
    private String value;



    public model_UserProperty(
        String global_,        String user,        String default,        String value    ) {
        super(
        );
        this.global_ = global_;
        this.user = user;
        this.default = default;
        this.value = value;
    }


    public String getGlobal_() {
        return global_;
    }

    public void setGlobal_(String global_) {
        this.global_ = global_;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}