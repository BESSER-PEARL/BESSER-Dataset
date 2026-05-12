





import java.util.List;
import java.util.ArrayList;

public class FAVORITES  {

    private String statusId;
    private String createdAt;
    private String _id;
    private String userId;
    private String storeId;





    private USER user;




    private STORE store;


    public FAVORITES(
        String statusId,        String createdAt,        String _id,        String userId,        String storeId    ) {
        this.statusId = statusId;
        this.createdAt = createdAt;
        this._id = _id;
        this.userId = userId;
        this.storeId = storeId;
    }


    public String getStatusid() {
        return statusId;
    }

    public void setStatusid(String statusId) {
        this.statusId = statusId;
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
    public String getStoreid() {
        return storeId;
    }

    public void setStoreid(String storeId) {
        this.storeId = storeId;
    }

    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }
    public STORE getStore() {
        return store;
    }

    public void setStore(STORE store) {
        this.store = store;
    }

}