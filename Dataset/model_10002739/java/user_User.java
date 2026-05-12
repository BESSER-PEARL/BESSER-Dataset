





import java.util.List;
import java.util.ArrayList;

public class user_User  {

    private None interests;
    private None address;
    private None reviews;
    private None business;
    private None wishlist;
    private None id;
    private String displayName;
    private String email;
    private None lastName;
    private None fiirstName;
    private None phone;
    private None provider;
    private None purchaseHistory;
    private String photoURL;



    public user_User(
        None interests,        None address,        None reviews,        None business,        None wishlist,        None id,        String displayName,        String email,        None lastName,        None fiirstName,        None phone,        None provider,        None purchaseHistory,        String photoURL    ) {
        this.interests = interests;
        this.address = address;
        this.reviews = reviews;
        this.business = business;
        this.wishlist = wishlist;
        this.id = id;
        this.displayName = displayName;
        this.email = email;
        this.lastName = lastName;
        this.fiirstName = fiirstName;
        this.phone = phone;
        this.provider = provider;
        this.purchaseHistory = purchaseHistory;
        this.photoURL = photoURL;
    }


    public None getInterests() {
        return interests;
    }

    public void setInterests(None interests) {
        this.interests = interests;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public None getBusiness() {
        return business;
    }

    public void setBusiness(None business) {
        this.business = business;
    }
    public None getWishlist() {
        return wishlist;
    }

    public void setWishlist(None wishlist) {
        this.wishlist = wishlist;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public None getLastname() {
        return lastName;
    }

    public void setLastname(None lastName) {
        this.lastName = lastName;
    }
    public None getFiirstname() {
        return fiirstName;
    }

    public void setFiirstname(None fiirstName) {
        this.fiirstName = fiirstName;
    }
    public None getPhone() {
        return phone;
    }

    public void setPhone(None phone) {
        this.phone = phone;
    }
    public None getProvider() {
        return provider;
    }

    public void setProvider(None provider) {
        this.provider = provider;
    }
    public None getPurchasehistory() {
        return purchaseHistory;
    }

    public void setPurchasehistory(None purchaseHistory) {
        this.purchaseHistory = purchaseHistory;
    }
    public String getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(String photoURL) {
        this.photoURL = photoURL;
    }


}