





import java.util.List;
import java.util.ArrayList;

public class myDsl_ActionCreator extends AbstractFrontElement {

    private String type;
    private String name;





    private myDsl_Action mydsl_action;


    public myDsl_ActionCreator(
        String type,        String name    ) {
        super(
        );
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

    public myDsl_Action getMydsl_action() {
        return mydsl_action;
    }

    public void setMydsl_action(myDsl_Action mydsl_action) {
        this.mydsl_action = mydsl_action;
    }

}