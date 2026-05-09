





import java.util.List;
import java.util.ArrayList;

public class myDsl_ActionDispatcher extends AbstractFrontElement {

    private String name;





    private myDsl_Action mydsl_action;




    private myDsl_ActionCreator mydsl_actioncreator;


    public myDsl_ActionDispatcher(
        String name    ) {
        super(
        );
        this.name = name;
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
    public myDsl_ActionCreator getMydsl_actioncreator() {
        return mydsl_actioncreator;
    }

    public void setMydsl_actioncreator(myDsl_ActionCreator mydsl_actioncreator) {
        this.mydsl_actioncreator = mydsl_actioncreator;
    }

}