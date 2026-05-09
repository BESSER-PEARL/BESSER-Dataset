





import java.util.List;
import java.util.ArrayList;

public class cpsml_Function  {

    private String name;





    private cpsml_DeVariable cpsml_devariable;




    private cpsml_IndeVariable cpsml_indevariable;




    private cpsml_ODE cpsml_ode;


    public cpsml_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cpsml_DeVariable getCpsml_devariable() {
        return cpsml_devariable;
    }

    public void setCpsml_devariable(cpsml_DeVariable cpsml_devariable) {
        this.cpsml_devariable = cpsml_devariable;
    }
    public cpsml_IndeVariable getCpsml_indevariable() {
        return cpsml_indevariable;
    }

    public void setCpsml_indevariable(cpsml_IndeVariable cpsml_indevariable) {
        this.cpsml_indevariable = cpsml_indevariable;
    }
    public cpsml_ODE getCpsml_ode() {
        return cpsml_ode;
    }

    public void setCpsml_ode(cpsml_ODE cpsml_ode) {
        this.cpsml_ode = cpsml_ode;
    }

}