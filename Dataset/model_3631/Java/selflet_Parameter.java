





import java.util.List;
import java.util.ArrayList;

public class selflet_Parameter  {

    private String type;
    private String name;





    private selflet_Input selflet_input;


    public selflet_Parameter(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public selflet_Input getSelflet_input() {
        return selflet_input;
    }

    public void setSelflet_input(selflet_Input selflet_input) {
        this.selflet_input = selflet_input;
    }

}