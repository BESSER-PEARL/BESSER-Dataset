





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_ActionMethodType  {

    private String type;
    private String name;
    private String many;





    private giraffeDSL_Action giraffedsl_action;


    public giraffeDSL_ActionMethodType(
        String type,        String name,        String many    ) {
        this.type = type;
        this.name = name;
        this.many = many;
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
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }

    public giraffeDSL_Action getGiraffedsl_action() {
        return giraffedsl_action;
    }

    public void setGiraffedsl_action(giraffeDSL_Action giraffedsl_action) {
        this.giraffedsl_action = giraffedsl_action;
    }

}