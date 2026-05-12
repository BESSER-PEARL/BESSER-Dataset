





import java.util.List;
import java.util.ArrayList;

public class REFUND  {

    private String productId;
    private String _id;
    private String title;
    private String storeId;
    private String created_at;
    private String message;
    private String shoppingHistoryId;
    private String userId;





    private SHOPPING_HISTORY shopping_history;


    public REFUND(
        String productId,        String _id,        String title,        String storeId,        String created_at,        String message,        String shoppingHistoryId,        String userId    ) {
        this.productId = productId;
        this._id = _id;
        this.title = title;
        this.storeId = storeId;
        this.created_at = created_at;
        this.message = message;
        this.shoppingHistoryId = shoppingHistoryId;
        this.userId = userId;
    }


    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getStoreid() {
        return storeId;
    }

    public void setStoreid(String storeId) {
        this.storeId = storeId;
    }
    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getShoppinghistoryid() {
        return shoppingHistoryId;
    }

    public void setShoppinghistoryid(String shoppingHistoryId) {
        this.shoppingHistoryId = shoppingHistoryId;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }

    public SHOPPING_HISTORY getShopping_history() {
        return shopping_history;
    }

    public void setShopping_history(SHOPPING_HISTORY shopping_history) {
        this.shopping_history = shopping_history;
    }

}