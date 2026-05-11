





import java.util.List;
import java.util.ArrayList;

public class roverml_Component extends NamedElement {

    private String kind;





    private roverml_Rover roverml_rover;


    public roverml_Component(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public roverml_Rover getRoverml_rover() {
        return roverml_rover;
    }

    public void setRoverml_rover(roverml_Rover roverml_rover) {
        this.roverml_rover = roverml_rover;
    }

}