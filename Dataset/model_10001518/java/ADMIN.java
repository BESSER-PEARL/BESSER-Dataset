





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String NAME;
    private String PASSWORD;



    public ADMIN(
        String NAME,        String PASSWORD    ) {
        this.NAME = NAME;
        this.PASSWORD = PASSWORD;
    }


    public String getName() {
        return NAME;
    }

    public void setName(String NAME) {
        this.NAME = NAME;
    }
    public String getPassword() {
        return PASSWORD;
    }

    public void setPassword(String PASSWORD) {
        this.PASSWORD = PASSWORD;
    }


}