





import java.util.List;
import java.util.ArrayList;

public class Usuario  {

    private String Last_Name;
    private String Password;
    private int ID_Number;
    private String First_Name;



    public Usuario(
        String Last_Name,        String Password,        int ID_Number,        String First_Name    ) {
        this.Last_Name = Last_Name;
        this.Password = Password;
        this.ID_Number = ID_Number;
        this.First_Name = First_Name;
    }


    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getId_number() {
        return ID_Number;
    }

    public void setId_number(int ID_Number) {
        this.ID_Number = ID_Number;
    }
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
    }


}