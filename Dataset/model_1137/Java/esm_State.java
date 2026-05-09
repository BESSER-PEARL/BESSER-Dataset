





import java.util.List;
import java.util.ArrayList;

public class esm_State  {

    private String name;





    private esm_Machine esm_machine;


    public esm_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public esm_Machine getEsm_machine() {
        return esm_machine;
    }

    public void setEsm_machine(esm_Machine esm_machine) {
        this.esm_machine = esm_machine;
    }

}