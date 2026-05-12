





import java.util.List;
import java.util.ArrayList;

public class user_Business  {

    private String website;
    private String name;
    private None staffUsers;
    private None adminUser;
    private String category;
    private None products;
    private None address;
    private String id;
    private String avgRatings;
    private None tags;
    private String phone;
    private String email;



    public user_Business(
        String website,        String name,        None staffUsers,        None adminUser,        String category,        None products,        None address,        String id,        String avgRatings,        None tags,        String phone,        String email    ) {
        this.website = website;
        this.name = name;
        this.staffUsers = staffUsers;
        this.adminUser = adminUser;
        this.category = category;
        this.products = products;
        this.address = address;
        this.id = id;
        this.avgRatings = avgRatings;
        this.tags = tags;
        this.phone = phone;
        this.email = email;
    }


    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getStaffusers() {
        return staffUsers;
    }

    public void setStaffusers(None staffUsers) {
        this.staffUsers = staffUsers;
    }
    public None getAdminuser() {
        return adminUser;
    }

    public void setAdminuser(None adminUser) {
        this.adminUser = adminUser;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getProducts() {
        return products;
    }

    public void setProducts(None products) {
        this.products = products;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAvgratings() {
        return avgRatings;
    }

    public void setAvgratings(String avgRatings) {
        this.avgRatings = avgRatings;
    }
    public None getTags() {
        return tags;
    }

    public void setTags(None tags) {
        this.tags = tags;
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


}