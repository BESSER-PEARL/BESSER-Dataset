





import java.util.List;
import java.util.ArrayList;

public class Classes_StaffMember extends IPerson {

    private boolean isLoggedIn;
    private String password;
    private String admin;
    private String username;





    private Classes_IHotelManagerImpl classes_ihotelmanagerimpl;


    public Classes_StaffMember(
        boolean isLoggedIn,        String password,        String admin,        String username    ) {
        super(
        );
        this.isLoggedIn = isLoggedIn;
        this.password = password;
        this.admin = admin;
        this.username = username;
    }


    public boolean getIsloggedin() {
        return isLoggedIn;
    }

    public void setIsloggedin(boolean isLoggedIn) {
        this.isLoggedIn = isLoggedIn;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAdmin() {
        return admin;
    }

    public void setAdmin(String admin) {
        this.admin = admin;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Classes_IHotelManagerImpl getClasses_ihotelmanagerimpl() {
        return classes_ihotelmanagerimpl;
    }

    public void setClasses_ihotelmanagerimpl(Classes_IHotelManagerImpl classes_ihotelmanagerimpl) {
        this.classes_ihotelmanagerimpl = classes_ihotelmanagerimpl;
    }

}