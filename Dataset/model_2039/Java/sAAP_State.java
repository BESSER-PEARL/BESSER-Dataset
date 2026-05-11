





import java.util.List;
import java.util.ArrayList;

public class sAAP_State  {

    private String name;
    private boolean default;



    public sAAP_State(
        String name,        boolean default    ) {
        this.name = name;
        this.default = default;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }


}