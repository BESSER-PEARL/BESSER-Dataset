





import java.util.List;
import java.util.ArrayList;

public class Abstract_Door  {

    private String Automatic;
    private String Materials;
    private String Security;



    public Abstract_Door(
        String Automatic,        String Materials,        String Security    ) {
        this.Automatic = Automatic;
        this.Materials = Materials;
        this.Security = Security;
    }


    public String getAutomatic() {
        return Automatic;
    }

    public void setAutomatic(String Automatic) {
        this.Automatic = Automatic;
    }
    public String getMaterials() {
        return Materials;
    }

    public void setMaterials(String Materials) {
        this.Materials = Materials;
    }
    public String getSecurity() {
        return Security;
    }

    public void setSecurity(String Security) {
        this.Security = Security;
    }


}