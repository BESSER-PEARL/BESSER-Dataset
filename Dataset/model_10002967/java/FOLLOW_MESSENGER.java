





import java.util.List;
import java.util.ArrayList;

public class FOLLOW_MESSENGER  {

    private String userId;
    private String createdAt;
    private String _id;



    public FOLLOW_MESSENGER(
        String userId,        String createdAt,        String _id    ) {
        this.userId = userId;
        this.createdAt = createdAt;
        this._id = _id;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }


}