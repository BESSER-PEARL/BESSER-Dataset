





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String FirstName;
    private String PhoneNumber;
    private String LastName;
    private String Email;
    private String Password;
    private int Role;
    private String Login;





    private CouponCode couponcode;




    private FavoriteItem favoriteitem;


    public User(
        String FirstName,        String PhoneNumber,        String LastName,        String Email,        String Password,        int Role,        String Login    ) {
        this.FirstName = FirstName;
        this.PhoneNumber = PhoneNumber;
        this.LastName = LastName;
        this.Email = Email;
        this.Password = Password;
        this.Role = Role;
        this.Login = Login;
    }


    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getRole() {
        return Role;
    }

    public void setRole(int Role) {
        this.Role = Role;
    }
    public String getLogin() {
        return Login;
    }

    public void setLogin(String Login) {
        this.Login = Login;
    }

    public CouponCode getCouponcode() {
        return couponcode;
    }

    public void setCouponcode(CouponCode couponcode) {
        this.couponcode = couponcode;
    }
    public FavoriteItem getFavoriteitem() {
        return favoriteitem;
    }

    public void setFavoriteitem(FavoriteItem favoriteitem) {
        this.favoriteitem = favoriteitem;
    }

}