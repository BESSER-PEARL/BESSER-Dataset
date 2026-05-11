





import java.util.List;
import java.util.ArrayList;

public class farrusco_Behavior extends Node {

    private String Name;





    private farrusco_Filho farrusco_filho;


    public farrusco_Behavior(
        String Name    ) {
        super(
        );
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public farrusco_Filho getFarrusco_filho() {
        return farrusco_filho;
    }

    public void setFarrusco_filho(farrusco_Filho farrusco_filho) {
        this.farrusco_filho = farrusco_filho;
    }

}