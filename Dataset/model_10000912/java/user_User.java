





import java.util.List;
import java.util.ArrayList;

public class user_User  {

    private None address;
    private None lastName;
    private None phone;
    private None wishlist;
    private None id;
    private String displayName;
    private None interests;
    private None business;
    private None provider;
    private None purchaseHistory;
    private String photoURL;
    private None reviews;
    private None fiirstName;
    private String email;



    public user_User(
        None address,        None lastName,        None phone,        None wishlist,        None id,        String displayName,        None interests,        None business,        None provider,        None purchaseHistory,        String photoURL,        None reviews,        None fiirstName,        String email    ) {
        this.address = address;
        this.lastName = lastName;
        this.phone = phone;
        this.wishlist = wishlist;
        this.id = id;
        this.displayName = displayName;
        this.interests = interests;
        this.business = business;
        this.provider = provider;
        this.purchaseHistory = purchaseHistory;
        this.photoURL = photoURL;
        this.reviews = reviews;
        this.fiirstName = fiirstName;
        this.email = email;
    }


    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getLastname() {
        return lastName;
    }

    public void setLastname(None lastName) {
        this.lastName = lastName;
    }
    public None getPhone() {
        return phone;
    }

    public void setPhone(None phone) {
        this.phone = phone;
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
    public None getInterests() {
        return interests;
    }

    public void setInterests(None interests) {
        this.interests = interests;
    }
    public None getBusiness() {
        return business;
    }

    public void setBusiness(None business) {
        this.business = business;
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
    public None getReviews() {
        return reviews;
    }

    public void setReviews(None reviews) {
        this.reviews = reviews;
    }
    public None getFiirstname() {
        return fiirstName;
    }

    public void setFiirstname(None fiirstName) {
        this.fiirstName = fiirstName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}