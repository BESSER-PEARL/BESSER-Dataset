





import java.util.List;
import java.util.ArrayList;

public class Docbook_AddressType  {

    private String format;
    private String state;
    private String email;



    public Docbook_AddressType(
        String format,        String state,        String email    ) {
        this.format = format;
        this.state = state;
        this.email = email;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}