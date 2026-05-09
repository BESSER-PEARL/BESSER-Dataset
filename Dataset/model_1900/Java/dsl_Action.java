





import java.util.List;
import java.util.ArrayList;

public class dsl_Action extends AbstractFrontElement {

    private String name;





    private dsl_Directory dsl_directory;




    private dsl_ActionDispatcher dsl_actiondispatcher;




    private dsl_ActionCreator dsl_actioncreator;


    public dsl_Action(
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

    public dsl_Directory getDsl_directory() {
        return dsl_directory;
    }

    public void setDsl_directory(dsl_Directory dsl_directory) {
        this.dsl_directory = dsl_directory;
    }
    public dsl_ActionDispatcher getDsl_actiondispatcher() {
        return dsl_actiondispatcher;
    }

    public void setDsl_actiondispatcher(dsl_ActionDispatcher dsl_actiondispatcher) {
        this.dsl_actiondispatcher = dsl_actiondispatcher;
    }
    public dsl_ActionCreator getDsl_actioncreator() {
        return dsl_actioncreator;
    }

    public void setDsl_actioncreator(dsl_ActionCreator dsl_actioncreator) {
        this.dsl_actioncreator = dsl_actioncreator;
    }

}