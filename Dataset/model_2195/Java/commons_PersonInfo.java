





import java.util.List;
import java.util.ArrayList;

public class commons_PersonInfo extends PersonLike, NameContainer, Sluggable, PhotoIdContainer, Identifiable {

    private String mobileNumber;
    private String email;
    private String gender;



    public commons_PersonInfo(
        String mobileNumber,        String email,        String gender    ) {
        super(
        );
        this.mobileNumber = mobileNumber;
        this.email = email;
        this.gender = gender;
    }


    public String getMobilenumber() {
        return mobileNumber;
    }

    public void setMobilenumber(String mobileNumber) {
        this.mobileNumber = mobileNumber;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }


}