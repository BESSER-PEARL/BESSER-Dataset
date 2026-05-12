





import java.util.List;
import java.util.ArrayList;

public class UserAddress  {

    private String StreetName;
    private int StreetNum;
    private String PostCode;
    private String City;





    private User_Account user_account;


    public UserAddress(
        String StreetName,        int StreetNum,        String PostCode,        String City    ) {
        this.StreetName = StreetName;
        this.StreetNum = StreetNum;
        this.PostCode = PostCode;
        this.City = City;
    }


    public String getStreetname() {
        return StreetName;
    }

    public void setStreetname(String StreetName) {
        this.StreetName = StreetName;
    }
    public int getStreetnum() {
        return StreetNum;
    }

    public void setStreetnum(int StreetNum) {
        this.StreetNum = StreetNum;
    }
    public String getPostcode() {
        return PostCode;
    }

    public void setPostcode(String PostCode) {
        this.PostCode = PostCode;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }

    public User_Account getUser_account() {
        return user_account;
    }

    public void setUser_account(User_Account user_account) {
        this.user_account = user_account;
    }

}