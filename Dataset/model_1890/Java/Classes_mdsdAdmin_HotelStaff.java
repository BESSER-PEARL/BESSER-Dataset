





import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdAdmin_HotelStaff  {

    private String Name;
    private int rank;
    private String SSN;
    private boolean isLoggedIn;
    private String password;



    public Classes_mdsdAdmin_HotelStaff(
        String Name,        int rank,        String SSN,        boolean isLoggedIn,        String password    ) {
        this.Name = Name;
        this.rank = rank;
        this.SSN = SSN;
        this.isLoggedIn = isLoggedIn;
        this.password = password;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    public String getSsn() {
        return SSN;
    }

    public void setSsn(String SSN) {
        this.SSN = SSN;
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


}