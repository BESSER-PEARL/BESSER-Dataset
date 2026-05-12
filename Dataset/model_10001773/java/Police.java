





import java.util.List;
import java.util.ArrayList;

public class Police  {

    private String name;





    private Home_Security_System home_security_system;


    public Police(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Home_Security_System getHome_security_system() {
        return home_security_system;
    }

    public void setHome_security_system(Home_Security_System home_security_system) {
        this.home_security_system = home_security_system;
    }

}