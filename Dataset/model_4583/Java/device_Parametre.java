





import java.util.List;
import java.util.ArrayList;

public class device_Parametre  {

    private String name;





    private device_Fonctionnalite device_fonctionnalite;


    public device_Parametre(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public device_Fonctionnalite getDevice_fonctionnalite() {
        return device_fonctionnalite;
    }

    public void setDevice_fonctionnalite(device_Fonctionnalite device_fonctionnalite) {
        this.device_fonctionnalite = device_fonctionnalite;
    }

}