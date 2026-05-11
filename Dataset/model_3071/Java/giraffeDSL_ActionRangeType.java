





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_ActionRangeType  {

    private String type;
    private String many;
    private String name;





    private giraffeDSL_Action giraffedsl_action;


    public giraffeDSL_ActionRangeType(
        String type,        String many,        String name    ) {
        this.type = type;
        this.many = many;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public giraffeDSL_Action getGiraffedsl_action() {
        return giraffedsl_action;
    }

    public void setGiraffedsl_action(giraffeDSL_Action giraffedsl_action) {
        this.giraffedsl_action = giraffedsl_action;
    }

}