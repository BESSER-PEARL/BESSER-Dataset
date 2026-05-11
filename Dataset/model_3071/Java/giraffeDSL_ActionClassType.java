





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_ActionClassType  {

    private String name;
    private String many;
    private String type;





    private giraffeDSL_Action giraffedsl_action;


    public giraffeDSL_ActionClassType(
        String name,        String many,        String type    ) {
        this.name = name;
        this.many = many;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public giraffeDSL_Action getGiraffedsl_action() {
        return giraffedsl_action;
    }

    public void setGiraffedsl_action(giraffeDSL_Action giraffedsl_action) {
        this.giraffedsl_action = giraffedsl_action;
    }

}