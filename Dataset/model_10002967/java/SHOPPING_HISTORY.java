





import java.util.List;
import java.util.ArrayList;

public class SHOPPING_HISTORY  {

    private int score;
    private boolean isNew;
    private String storeId;
    private String description;
    private String _id;
    private String userId;
    private String note;
    private String name;
    private String shipArrival;
    private String productId;
    private String photos;
    private int price;
    private int sold;
    private boolean isSold;
    private String comment;
    private String shipName;
    private String shipAddress;
    private String created_at;
    private int shipPrice;
    private int quantity;
    private String attribute;
    private String status;
    private String STATUS_SHOPPING_HIST_ID;





    private PRODUCT product;




    private USER user;


    public SHOPPING_HISTORY(
        int score,        boolean isNew,        String storeId,        String description,        String _id,        String userId,        String note,        String name,        String shipArrival,        String productId,        String photos,        int price,        int sold,        boolean isSold,        String comment,        String shipName,        String shipAddress,        String created_at,        int shipPrice,        int quantity,        String attribute,        String status,        String STATUS_SHOPPING_HIST_ID    ) {
        this.score = score;
        this.isNew = isNew;
        this.storeId = storeId;
        this.description = description;
        this._id = _id;
        this.userId = userId;
        this.note = note;
        this.name = name;
        this.shipArrival = shipArrival;
        this.productId = productId;
        this.photos = photos;
        this.price = price;
        this.sold = sold;
        this.isSold = isSold;
        this.comment = comment;
        this.shipName = shipName;
        this.shipAddress = shipAddress;
        this.created_at = created_at;
        this.shipPrice = shipPrice;
        this.quantity = quantity;
        this.attribute = attribute;
        this.status = status;
        this.STATUS_SHOPPING_HIST_ID = STATUS_SHOPPING_HIST_ID;
    }


    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public boolean getIsnew() {
        return isNew;
    }

    public void setIsnew(boolean isNew) {
        this.isNew = isNew;
    }
    public String getStoreid() {
        return storeId;
    }

    public void setStoreid(String storeId) {
        this.storeId = storeId;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShiparrival() {
        return shipArrival;
    }

    public void setShiparrival(String shipArrival) {
        this.shipArrival = shipArrival;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getSold() {
        return sold;
    }

    public void setSold(int sold) {
        this.sold = sold;
    }
    public boolean getIssold() {
        return isSold;
    }

    public void setIssold(boolean isSold) {
        this.isSold = isSold;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getShipname() {
        return shipName;
    }

    public void setShipname(String shipName) {
        this.shipName = shipName;
    }
    public String getShipaddress() {
        return shipAddress;
    }

    public void setShipaddress(String shipAddress) {
        this.shipAddress = shipAddress;
    }
    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }
    public int getShipprice() {
        return shipPrice;
    }

    public void setShipprice(int shipPrice) {
        this.shipPrice = shipPrice;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getStatus_shopping_hist_id() {
        return STATUS_SHOPPING_HIST_ID;
    }

    public void setStatus_shopping_hist_id(String STATUS_SHOPPING_HIST_ID) {
        this.STATUS_SHOPPING_HIST_ID = STATUS_SHOPPING_HIST_ID;
    }

    public PRODUCT getProduct() {
        return product;
    }

    public void setProduct(PRODUCT product) {
        this.product = product;
    }
    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}