





import java.util.List;
import java.util.ArrayList;

public class user_User  {

    private None address;
    private None interests;
    private String fiirstName;
    private None wishlist;
    private None purchaseHistory;
    private String phone;
    private String email;
    private None reviews;
    private String photoURL;
    private String displayName;
    private None provider;
    private String lastName;
    private None business;
    private String id;



    public user_User(
        None address,        None interests,        String fiirstName,        None wishlist,        None purchaseHistory,        String phone,        String email,        None reviews,        String photoURL,        String displayName,        None provider,        String lastName,        None business,        String id    ) {
        this.address = address;
        this.interests = interests;
        this.fiirstName = fiirstName;
        this.wishlist = wishlist;
        this.purchaseHistory = purchaseHistory;
        this.phone = phone;
        this.email = email;
        this.reviews = reviews;
        this.photoURL = photoURL;
        this.displayName = displayName;
        this.provider = provider;
        this.lastName = lastName;
        this.business = business;
        this.id = id;
    }


    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getInterests() {
        return interests;
    }

    public void setInterests(None interests) {
        this.interests = interests;
    }
    public String getFiirstname() {
        return fiirstName;
    }

    public void setFiirstname(String fiirstName) {
        this.fiirstName = fiirstName;
    }
    public None getWishlist() {
        return wishlist;
    }

    public void setWishlist(None wishlist) {
        this.wishlist = wishlist;
    }
    public None getPurchasehistory() {
        return purchaseHistory;
    }

    public void setPurchasehistory(None purchaseHistory) {
        this.purchaseHistory = purchaseHistory;
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
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public String getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(String photoURL) {
        this.photoURL = photoURL;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public None getProvider() {
        return provider;
    }

    public void setProvider(None provider) {
        this.provider = provider;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public None getBusiness() {
        return business;
    }

    public void setBusiness(None business) {
        this.business = business;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}