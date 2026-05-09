





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_User  {

    private String md5Pwd;
    private String userType;
    private String userName;





    private reservationsystem_Person reservationsystem_person;


    public reservationsystem_User(
        String md5Pwd,        String userType,        String userName    ) {
        this.md5Pwd = md5Pwd;
        this.userType = userType;
        this.userName = userName;
    }


    public String getMd5pwd() {
        return md5Pwd;
    }

    public void setMd5pwd(String md5Pwd) {
        this.md5Pwd = md5Pwd;
    }
    public String getUsertype() {
        return userType;
    }

    public void setUsertype(String userType) {
        this.userType = userType;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public reservationsystem_Person getReservationsystem_person() {
        return reservationsystem_person;
    }

    public void setReservationsystem_person(reservationsystem_Person reservationsystem_person) {
        this.reservationsystem_person = reservationsystem_person;
    }

}