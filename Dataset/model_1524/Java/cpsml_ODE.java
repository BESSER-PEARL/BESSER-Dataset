





import java.util.List;
import java.util.ArrayList;

public class cpsml_ODE  {

    private String name;





    private cpsml_State cpsml_state;




    private cpsml_System cpsml_system;




    private cpsml_State cpsml_state;


    public cpsml_ODE(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cpsml_State getCpsml_state() {
        return cpsml_state;
    }

    public void setCpsml_state(cpsml_State cpsml_state) {
        this.cpsml_state = cpsml_state;
    }
    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public cpsml_State getCpsml_state() {
        return cpsml_state;
    }

    public void setCpsml_state(cpsml_State cpsml_state) {
        this.cpsml_state = cpsml_state;
    }

}