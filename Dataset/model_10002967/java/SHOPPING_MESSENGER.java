





import java.util.List;
import java.util.ArrayList;

public class SHOPPING_MESSENGER  {

    private String userId;
    private String _id;
    private String created_at;
    private String photos;
    private String message;
    private String storeId;





    private SHOPPING_HISTORY shopping_history;


    public SHOPPING_MESSENGER(
        String userId,        String _id,        String created_at,        String photos,        String message,        String storeId    ) {
        this.userId = userId;
        this._id = _id;
        this.created_at = created_at;
        this.photos = photos;
        this.message = message;
        this.storeId = storeId;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getStoreid() {
        return storeId;
    }

    public void setStoreid(String storeId) {
        this.storeId = storeId;
    }

    public SHOPPING_HISTORY getShopping_history() {
        return shopping_history;
    }

    public void setShopping_history(SHOPPING_HISTORY shopping_history) {
        this.shopping_history = shopping_history;
    }

}