





import java.util.List;
import java.util.ArrayList;

public class cpsml_Condition  {

    private String name;





    private cpsml_ODE cpsml_ode;


    public cpsml_Condition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cpsml_ODE getCpsml_ode() {
        return cpsml_ode;
    }

    public void setCpsml_ode(cpsml_ODE cpsml_ode) {
        this.cpsml_ode = cpsml_ode;
    }

}