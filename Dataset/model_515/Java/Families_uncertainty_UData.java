





import java.util.List;
import java.util.ArrayList;

public class Families_uncertainty_UData  {

    private String utype;
    private String name;



    public Families_uncertainty_UData(
        String utype,        String name    ) {
        this.utype = utype;
        this.name = name;
    }


    public String getUtype() {
        return utype;
    }

    public void setUtype(String utype) {
        this.utype = utype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}