





import java.util.List;
import java.util.ArrayList;

public class PASSENGER  {

    private int Pass_ID;
    private String Pass_Name;
    private String Pass_Address;



    public PASSENGER(
        int Pass_ID,        String Pass_Name,        String Pass_Address    ) {
        this.Pass_ID = Pass_ID;
        this.Pass_Name = Pass_Name;
        this.Pass_Address = Pass_Address;
    }


    public int getPass_id() {
        return Pass_ID;
    }

    public void setPass_id(int Pass_ID) {
        this.Pass_ID = Pass_ID;
    }
    public String getPass_name() {
        return Pass_Name;
    }

    public void setPass_name(String Pass_Name) {
        this.Pass_Name = Pass_Name;
    }
    public String getPass_address() {
        return Pass_Address;
    }

    public void setPass_address(String Pass_Address) {
        this.Pass_Address = Pass_Address;
    }


}