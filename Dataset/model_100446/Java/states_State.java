





import java.util.List;
import java.util.ArrayList;

public class states_State  {

    private boolean initial;
    private String name;



    public states_State(
        boolean initial,        String name    ) {
        this.initial = initial;
        this.name = name;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}