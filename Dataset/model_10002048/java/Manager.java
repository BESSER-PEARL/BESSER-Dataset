





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String Name;
    private String ContatctNo;
    private int ManagerID;
    private String Email;



    public Manager(
        String Name,        String ContatctNo,        int ManagerID,        String Email    ) {
        this.Name = Name;
        this.ContatctNo = ContatctNo;
        this.ManagerID = ManagerID;
        this.Email = Email;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getContatctno() {
        return ContatctNo;
    }

    public void setContatctno(String ContatctNo) {
        this.ContatctNo = ContatctNo;
    }
    public int getManagerid() {
        return ManagerID;
    }

    public void setManagerid(int ManagerID) {
        this.ManagerID = ManagerID;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}