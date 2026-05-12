





import java.util.List;
import java.util.ArrayList;

public class User  {

    private None phone;
    private None lastName;
    private String id;
    private None address;
    private None firstName;
    private None email;
    private None photoURL;



    public User(
        None phone,        None lastName,        String id,        None address,        None firstName,        None email,        None photoURL    ) {
        this.phone = phone;
        this.lastName = lastName;
        this.id = id;
        this.address = address;
        this.firstName = firstName;
        this.email = email;
        this.photoURL = photoURL;
    }


    public None getPhone() {
        return phone;
    }

    public void setPhone(None phone) {
        this.phone = phone;
    }
    public None getLastname() {
        return lastName;
    }

    public void setLastname(None lastName) {
        this.lastName = lastName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getAddress() {
        return address;
    }

    public void setAddress(None address) {
        this.address = address;
    }
    public None getFirstname() {
        return firstName;
    }

    public void setFirstname(None firstName) {
        this.firstName = firstName;
    }
    public None getEmail() {
        return email;
    }

    public void setEmail(None email) {
        this.email = email;
    }
    public None getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(None photoURL) {
        this.photoURL = photoURL;
    }


}