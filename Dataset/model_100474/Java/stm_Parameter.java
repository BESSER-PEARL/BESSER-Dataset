





import java.util.List;
import java.util.ArrayList;

public class stm_Parameter  {

    private String name;
    private String type;





    private stm_Guard stm_guard;


    public stm_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public stm_Guard getStm_guard() {
        return stm_guard;
    }

    public void setStm_guard(stm_Guard stm_guard) {
        this.stm_guard = stm_guard;
    }

}