





import java.util.List;
import java.util.ArrayList;

public class bean_Friends  {

    private String email2;
    private String email1;



    public bean_Friends(
        String email2,        String email1    ) {
        this.email2 = email2;
        this.email1 = email1;
    }


    public String getEmail2() {
        return email2;
    }

    public void setEmail2(String email2) {
        this.email2 = email2;
    }
    public String getEmail1() {
        return email1;
    }

    public void setEmail1(String email1) {
        this.email1 = email1;
    }


}