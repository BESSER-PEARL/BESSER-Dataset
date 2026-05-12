





import java.util.List;
import java.util.ArrayList;

public class NOTIFICATION  {

    private String createdAt;
    private String _id;
    private String userId;
    private String message;
    private String code;





    private USER user;


    public NOTIFICATION(
        String createdAt,        String _id,        String userId,        String message,        String code    ) {
        this.createdAt = createdAt;
        this._id = _id;
        this.userId = userId;
        this.message = message;
        this.code = code;
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
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}