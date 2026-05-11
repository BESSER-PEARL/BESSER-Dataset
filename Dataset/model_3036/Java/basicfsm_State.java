





import java.util.List;
import java.util.ArrayList;

public class basicfsm_State  {

    private String name;





    private basicfsm_Machine basicfsm_machine;


    public basicfsm_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public basicfsm_Machine getBasicfsm_machine() {
        return basicfsm_machine;
    }

    public void setBasicfsm_machine(basicfsm_Machine basicfsm_machine) {
        this.basicfsm_machine = basicfsm_machine;
    }

}