





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_ModelElementEntity  {

    private String name;
    private String stereotype;



    public gestionmodelosconsultas_entitymodel_ModelElementEntity(
        String name,        String stereotype    ) {
        this.name = name;
        this.stereotype = stereotype;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }


}