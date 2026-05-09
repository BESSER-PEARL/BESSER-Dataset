





import java.util.List;
import java.util.ArrayList;

public class dsl_ActionDispatcher extends AbstractFrontElement {

    private String name;





    private dsl_ActionCreator dsl_actioncreator;


    public dsl_ActionDispatcher(
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

    public dsl_ActionCreator getDsl_actioncreator() {
        return dsl_actioncreator;
    }

    public void setDsl_actioncreator(dsl_ActionCreator dsl_actioncreator) {
        this.dsl_actioncreator = dsl_actioncreator;
    }

}