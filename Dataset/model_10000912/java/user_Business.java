





import java.util.List;
import java.util.ArrayList;

public class user_Business  {

    private String category;
    private String phone;
    private String email;
    private String website;
    private None id;
    private None products;
    private None avgRatings;
    private None name;
    private None adminUser;
    private None staffUsers;
    private None address;



    public user_Business(
        String category,        String phone,        String email,        String website,        None id,        None products,        None avgRatings,        None name,        None adminUser,        None staffUsers,        None address    ) {
        this.category = category;
        this.phone = phone;
        this.email = email;
        this.website = website;
        this.id = id;
        this.products = products;
        this.avgRatings = avgRatings;
        this.name = name;
        this.adminUser = adminUser;
        this.staffUsers = staffUsers;
        this.address = address;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public None getProducts() {
        return products;
    }

    public void setProducts(None products) {
        this.products = products;
    }
    public None getAvgratings() {
        return avgRatings;
    }

    public void setAvgratings(None avgRatings) {
        this.avgRatings = avgRatings;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public None getAdminuser() {
        return adminUser;
    }

    public void setAdminuser(None adminUser) {
        this.adminUser = adminUser;
    }
    public None getStaffusers() {
        return staffUsers;
    }

    public void setStaffusers(None staffUsers) {
        this.staffUsers = staffUsers;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }


}