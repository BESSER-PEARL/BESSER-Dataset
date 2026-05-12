





import java.util.List;
import java.util.ArrayList;

public class Driver  {

    private String avatar;
    private String username;
    private String email;
    private String phoneNumber;
    private int numberOfRatings;
    private String carLicense;
    private String averageRating;



    public Driver(
        String avatar,        String username,        String email,        String phoneNumber,        int numberOfRatings,        String carLicense,        String averageRating    ) {
        this.avatar = avatar;
        this.username = username;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.numberOfRatings = numberOfRatings;
        this.carLicense = carLicense;
        this.averageRating = averageRating;
    }


    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public int getNumberofratings() {
        return numberOfRatings;
    }

    public void setNumberofratings(int numberOfRatings) {
        this.numberOfRatings = numberOfRatings;
    }
    public String getCarlicense() {
        return carLicense;
    }

    public void setCarlicense(String carLicense) {
        this.carLicense = carLicense;
    }
    public String getAveragerating() {
        return averageRating;
    }

    public void setAveragerating(String averageRating) {
        this.averageRating = averageRating;
    }


}