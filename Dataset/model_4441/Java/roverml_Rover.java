





import java.util.List;
import java.util.ArrayList;

public class roverml_Rover extends NamedElement {






    private roverml_System roverml_system;




    private List<roverml_Component> roverml_components;




    private roverml_Program roverml_program;


    public roverml_Rover(
    ) {
        super(
        );
        this.roverml_components = new ArrayList<>();
    }

    public roverml_Rover(
        ArrayList<roverml_Component> roverml_components    ) {
        this.roverml_components = roverml_components;
    }


    public roverml_System getRoverml_system() {
        return roverml_system;
    }

    public void setRoverml_system(roverml_System roverml_system) {
        this.roverml_system = roverml_system;
    }
    public List<roverml_Component> getRoverml_components() {
        return roverml_components;
    }

    public void addRoverml_component(Roverml_component roverml_component) {
        this.roverml_components.add(roverml_component);
    }
    public roverml_Program getRoverml_program() {
        return roverml_program;
    }

    public void setRoverml_program(roverml_Program roverml_program) {
        this.roverml_program = roverml_program;
    }

}