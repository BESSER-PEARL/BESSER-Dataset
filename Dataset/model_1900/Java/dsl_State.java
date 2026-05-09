





import java.util.List;
import java.util.ArrayList;

public class dsl_State extends AbstractFrontElement {

    private String name;





    private dsl_Functionality dsl_functionality;




    private dsl_Reducer dsl_reducer;




    private dsl_Action dsl_action;


    public dsl_State(
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

    public dsl_Functionality getDsl_functionality() {
        return dsl_functionality;
    }

    public void setDsl_functionality(dsl_Functionality dsl_functionality) {
        this.dsl_functionality = dsl_functionality;
    }
    public dsl_Reducer getDsl_reducer() {
        return dsl_reducer;
    }

    public void setDsl_reducer(dsl_Reducer dsl_reducer) {
        this.dsl_reducer = dsl_reducer;
    }
    public dsl_Action getDsl_action() {
        return dsl_action;
    }

    public void setDsl_action(dsl_Action dsl_action) {
        this.dsl_action = dsl_action;
    }

}