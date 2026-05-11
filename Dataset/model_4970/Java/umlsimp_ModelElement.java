





import java.util.List;
import java.util.ArrayList;

public class umlsimp_ModelElement  {

    private String name;





    private umlsimp_Model umlsimp_model;


    public umlsimp_ModelElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlsimp_Model getUmlsimp_model() {
        return umlsimp_model;
    }

    public void setUmlsimp_model(umlsimp_Model umlsimp_model) {
        this.umlsimp_model = umlsimp_model;
    }

}