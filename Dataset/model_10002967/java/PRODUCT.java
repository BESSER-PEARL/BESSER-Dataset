





import java.util.List;
import java.util.ArrayList;

public class PRODUCT  {

    private String statusId;
    private boolean isNew;
    private String name;
    private int quantity;
    private String model;
    private String _id;
    private String description;
    private String relatedProducts;
    private String attribute;
    private int sold;
    private String storeId;
    private String photos;
    private String color;
    private int price;
    private String ShippingMethods;
    private String dimensions;
    private String createdAt;





    private List<USER> users;


    public PRODUCT(
        String statusId,        boolean isNew,        String name,        int quantity,        String model,        String _id,        String description,        String relatedProducts,        String attribute,        int sold,        String storeId,        String photos,        String color,        int price,        String ShippingMethods,        String dimensions,        String createdAt    ) {
        this.statusId = statusId;
        this.isNew = isNew;
        this.name = name;
        this.quantity = quantity;
        this.model = model;
        this._id = _id;
        this.description = description;
        this.relatedProducts = relatedProducts;
        this.attribute = attribute;
        this.sold = sold;
        this.storeId = storeId;
        this.photos = photos;
        this.color = color;
        this.price = price;
        this.ShippingMethods = ShippingMethods;
        this.dimensions = dimensions;
        this.createdAt = createdAt;
        this.users = new ArrayList<>();
    }

    public PRODUCT(
        String statusId,        boolean isNew,        String name,        int quantity,        String model,        String _id,        String description,        String relatedProducts,        String attribute,        int sold,        String storeId,        String photos,        String color,        int price,        String ShippingMethods,        String dimensions,        String createdAt        ArrayList<USER> users    ) {
        this.statusId = statusId;
        this.isNew = isNew;
        this.name = name;
        this.quantity = quantity;
        this.model = model;
        this._id = _id;
        this.description = description;
        this.relatedProducts = relatedProducts;
        this.attribute = attribute;
        this.sold = sold;
        this.storeId = storeId;
        this.photos = photos;
        this.color = color;
        this.price = price;
        this.ShippingMethods = ShippingMethods;
        this.dimensions = dimensions;
        this.createdAt = createdAt;
        this.users = users;
    }

    public String getStatusid() {
        return statusId;
    }

    public void setStatusid(String statusId) {
        this.statusId = statusId;
    }
    public boolean getIsnew() {
        return isNew;
    }

    public void setIsnew(boolean isNew) {
        this.isNew = isNew;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
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
    public String getRelatedproducts() {
        return relatedProducts;
    }

    public void setRelatedproducts(String relatedProducts) {
        this.relatedProducts = relatedProducts;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getSold() {
        return sold;
    }

    public void setSold(int sold) {
        this.sold = sold;
    }
    public String getStoreid() {
        return storeId;
    }

    public void setStoreid(String storeId) {
        this.storeId = storeId;
    }
    public String getPhotos() {
        return photos;
    }

    public void setPhotos(String photos) {
        this.photos = photos;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getShippingmethods() {
        return ShippingMethods;
    }

    public void setShippingmethods(String ShippingMethods) {
        this.ShippingMethods = ShippingMethods;
    }
    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }

    public List<USER> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}