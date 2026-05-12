





import java.util.List;
import java.util.ArrayList;

public class Lock_doors_sensors  {

    private String attribute;





    private Home_Security home_security;


    public Lock_doors_sensors(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Home_Security getHome_security() {
        return home_security;
    }

    public void setHome_security(Home_Security home_security) {
        this.home_security = home_security;
    }

}