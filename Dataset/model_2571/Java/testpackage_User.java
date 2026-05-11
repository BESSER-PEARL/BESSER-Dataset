





import java.util.List;
import java.util.ArrayList;

public class testpackage_User extends NamedElement {

    private String password;



    public testpackage_User(
        String password    ) {
        super(
        );
        this.password = password;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}