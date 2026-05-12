





import java.util.List;
import java.util.ArrayList;

public class HomeAutomation  {

    private String Lights;
    private String Apllicances;





    private Smart_mirror smart_mirror;


    public HomeAutomation(
        String Lights,        String Apllicances    ) {
        this.Lights = Lights;
        this.Apllicances = Apllicances;
    }


    public String getLights() {
        return Lights;
    }

    public void setLights(String Lights) {
        this.Lights = Lights;
    }
    public String getApllicances() {
        return Apllicances;
    }

    public void setApllicances(String Apllicances) {
        this.Apllicances = Apllicances;
    }

    public Smart_mirror getSmart_mirror() {
        return smart_mirror;
    }

    public void setSmart_mirror(Smart_mirror smart_mirror) {
        this.smart_mirror = smart_mirror;
    }

}