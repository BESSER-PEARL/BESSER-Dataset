





import java.util.List;
import java.util.ArrayList;

public class Docbook_AddressType  {

    private String email;
    private String state;
    private String format;



    public Docbook_AddressType(
        String email,        String state,        String format    ) {
        this.email = email;
        this.state = state;
        this.format = format;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}