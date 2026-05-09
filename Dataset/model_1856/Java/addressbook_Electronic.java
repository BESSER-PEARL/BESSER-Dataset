





import java.util.List;
import java.util.ArrayList;

public class addressbook_Electronic extends Contact {

    private String website;
    private String email;



    public addressbook_Electronic(
        String website,        String email    ) {
        super(
        );
        this.website = website;
        this.email = email;
    }


    public String getWebsite() {
        return website;
    }

    public void setWebsite(String website) {
        this.website = website;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}