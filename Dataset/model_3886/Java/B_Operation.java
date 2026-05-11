





import java.util.List;
import java.util.ArrayList;

public class B_Operation  {

    private String name;





    private B_Machine b_machine;


    public B_Operation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public B_Machine getB_machine() {
        return b_machine;
    }

    public void setB_machine(B_Machine b_machine) {
        this.b_machine = b_machine;
    }

}