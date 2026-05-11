





import java.util.List;
import java.util.ArrayList;

public class soaml_Property  {

    private String isID;





    private soaml_Property soaml_property;


    public soaml_Property(
        String isID    ) {
        this.isID = isID;
    }


    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }

    public soaml_Property getSoaml_property() {
        return soaml_property;
    }

    public void setSoaml_property(soaml_Property soaml_property) {
        this.soaml_property = soaml_property;
    }

}