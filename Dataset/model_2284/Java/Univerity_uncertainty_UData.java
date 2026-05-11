





import java.util.List;
import java.util.ArrayList;

public class Univerity_uncertainty_UData  {

    private String name;
    private String utype;



    public Univerity_uncertainty_UData(
        String name,        String utype    ) {
        this.name = name;
        this.utype = utype;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUtype() {
        return utype;
    }

    public void setUtype(String utype) {
        this.utype = utype;
    }


}