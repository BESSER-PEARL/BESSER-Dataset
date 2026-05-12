





import java.util.List;
import java.util.ArrayList;

public class user_Business  {

    private None products;
    private String website;
    private String description;
    private None name;
    private None staffUsers;
    private String email;
    private None gallery;
    private None address;
    private None avgRatings;
    private String logo;
    private None adminUser;
    private None providers;
    private None subCategories;
    private String category;
    private None id;
    private None tags;
    private None mapRef;
    private String phone;





    private List<user_Provider> user_providers;


    public user_Business(
        None products,        String website,        String description,        None name,        None staffUsers,        String email,        None gallery,        None address,        None avgRatings,        String logo,        None adminUser,        None providers,        None subCategories,        String category,        None id,        None tags,        None mapRef,        String phone    ) {
        this.products = products;
        this.website = website;
        this.description = description;
        this.name = name;
        this.staffUsers = staffUsers;
        this.email = email;
        this.gallery = gallery;
        this.address = address;
        this.avgRatings = avgRatings;
        this.logo = logo;
        this.adminUser = adminUser;
        this.providers = providers;
        this.subCategories = subCategories;
        this.category = category;
        this.id = id;
        this.tags = tags;
        this.mapRef = mapRef;
        this.phone = phone;
        this.user_providers = new ArrayList<>();
    }

    public user_Business(
        None products,        String website,        String description,        None name,        None staffUsers,        String email,        None gallery,        None address,        None avgRatings,        String logo,        None adminUser,        None providers,        None subCategories,        String category,        None id,        None tags,        None mapRef,        String phone        ArrayList<user_Provider> user_providers    ) {
        this.products = products;
        this.website = website;
        this.description = description;
        this.name = name;
        this.staffUsers = staffUsers;
        this.email = email;
        this.gallery = gallery;
        this.address = address;
        this.avgRatings = avgRatings;
        this.logo = logo;
        this.adminUser = adminUser;
        this.providers = providers;
        this.subCategories = subCategories;
        this.category = category;
        this.id = id;
        this.tags = tags;
        this.mapRef = mapRef;
        this.phone = phone;
        this.user_providers = user_providers;
    }

    public None getProducts() {
        return products;
    }

    public void setProducts(None products) {
        this.products = products;
    }
    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public None getStaffusers() {
        return staffUsers;
    }

    public void setStaffusers(None staffUsers) {
        this.staffUsers = staffUsers;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public None getGallery() {
        return gallery;
    }

    public void setGallery(None gallery) {
        this.gallery = gallery;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getAvgratings() {
        return avgRatings;
    }

    public void setAvgratings(None avgRatings) {
        this.avgRatings = avgRatings;
    }
    public String getLogo() {
        return logo;
    }

    public void setLogo(String logo) {
        this.logo = logo;
    }
    public None getAdminuser() {
        return adminUser;
    }

    public void setAdminuser(None adminUser) {
        this.adminUser = adminUser;
    }
    public None getProviders() {
        return providers;
    }

    public void setProviders(None providers) {
        this.providers = providers;
    }
    public None getSubcategories() {
        return subCategories;
    }

    public void setSubcategories(None subCategories) {
        this.subCategories = subCategories;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public None getTags() {
        return tags;
    }

    public void setTags(None tags) {
        this.tags = tags;
    }
    public None getMapref() {
        return mapRef;
    }

    public void setMapref(None mapRef) {
        this.mapRef = mapRef;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public List<user_Provider> getUser_providers() {
        return user_providers;
    }

    public void addUser_provider(User_provider user_provider) {
        this.user_providers.add(user_provider);
    }

}