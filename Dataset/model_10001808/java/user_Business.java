





import java.util.List;
import java.util.ArrayList;

public class user_Business  {

    private String website;
    private String email;
    private None id;
    private None address;
    private None products;
    private String phone;
    private String category;
    private None tags;
    private None name;
    private None adminUser;
    private None avgRatings;
    private None staffUsers;



    public user_Business(
        String website,        String email,        None id,        None address,        None products,        String phone,        String category,        None tags,        None name,        None adminUser,        None avgRatings,        None staffUsers    ) {
        this.website = website;
        this.email = email;
        this.id = id;
        this.address = address;
        this.products = products;
        this.phone = phone;
        this.category = category;
        this.tags = tags;
        this.name = name;
        this.adminUser = adminUser;
        this.avgRatings = avgRatings;
        this.staffUsers = staffUsers;
    }


    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getProducts() {
        return products;
    }

    public void setProducts(None products) {
        this.products = products;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getTags() {
        return tags;
    }

    public void setTags(None tags) {
        this.tags = tags;
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
    public None getAvgratings() {
        return avgRatings;
    }

    public void setAvgratings(None avgRatings) {
        this.avgRatings = avgRatings;
    }
    public None getStaffusers() {
        return staffUsers;
    }

    public void setStaffusers(None staffUsers) {
        this.staffUsers = staffUsers;
    }


}