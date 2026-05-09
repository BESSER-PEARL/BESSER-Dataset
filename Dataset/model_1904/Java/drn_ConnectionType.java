





import java.util.List;
import java.util.ArrayList;

public class drn_ConnectionType  {

    private String name;
    private String adress;





    private drn_Configuration drn_configuration;


    public drn_ConnectionType(
        String name,        String adress    ) {
        this.name = name;
        this.adress = adress;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }

    public drn_Configuration getDrn_configuration() {
        return drn_configuration;
    }

    public void setDrn_configuration(drn_Configuration drn_configuration) {
        this.drn_configuration = drn_configuration;
    }

}