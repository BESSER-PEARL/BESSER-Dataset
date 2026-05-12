





import java.util.List;
import java.util.ArrayList;

public class STORE  {

    private String createdAt;
    private String email;
    private String telephone;
    private String updateAt;
    private String _id;
    private String name;
    private String address;
    private String statusId;
    private String schedule;





    private SHOPPING_HISTORY shopping_history;




    private PRODUCT product;




    private USER user;


    public STORE(
        String createdAt,        String email,        String telephone,        String updateAt,        String _id,        String name,        String address,        String statusId,        String schedule    ) {
        this.createdAt = createdAt;
        this.email = email;
        this.telephone = telephone;
        this.updateAt = updateAt;
        this._id = _id;
        this.name = name;
        this.address = address;
        this.statusId = statusId;
        this.schedule = schedule;
    }


    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public String getUpdateat() {
        return updateAt;
    }

    public void setUpdateat(String updateAt) {
        this.updateAt = updateAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getStatusid() {
        return statusId;
    }

    public void setStatusid(String statusId) {
        this.statusId = statusId;
    }
    public String getSchedule() {
        return schedule;
    }

    public void setSchedule(String schedule) {
        this.schedule = schedule;
    }

    public SHOPPING_HISTORY getShopping_history() {
        return shopping_history;
    }

    public void setShopping_history(SHOPPING_HISTORY shopping_history) {
        this.shopping_history = shopping_history;
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