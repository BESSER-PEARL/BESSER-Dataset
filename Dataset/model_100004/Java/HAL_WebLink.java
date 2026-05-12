





import java.util.List;
import java.util.ArrayList;

public class HAL_WebLink extends AbstractDepotType {

    private String identifiant;



    public HAL_WebLink(
        String identifiant    ) {
        super(
        );
        this.identifiant = identifiant;
    }


    public String getIdentifiant() {
        return identifiant;
    }

    public void setIdentifiant(String identifiant) {
        this.identifiant = identifiant;
    }


}