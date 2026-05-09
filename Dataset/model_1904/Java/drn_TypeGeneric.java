





import java.util.List;
import java.util.ArrayList;

public class drn_TypeGeneric  {

    private String name;





    private drn_Configuration drn_configuration;


    public drn_TypeGeneric(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_Configuration getDrn_configuration() {
        return drn_configuration;
    }

    public void setDrn_configuration(drn_Configuration drn_configuration) {
        this.drn_configuration = drn_configuration;
    }

}