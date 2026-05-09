





import java.util.List;
import java.util.ArrayList;

public class myDsl_State extends AbstractFrontElement {

    private String name;





    private myDsl_Reducer mydsl_reducer;




    private myDsl_Action mydsl_action;


    public myDsl_State(
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

    public myDsl_Reducer getMydsl_reducer() {
        return mydsl_reducer;
    }

    public void setMydsl_reducer(myDsl_Reducer mydsl_reducer) {
        this.mydsl_reducer = mydsl_reducer;
    }
    public myDsl_Action getMydsl_action() {
        return mydsl_action;
    }

    public void setMydsl_action(myDsl_Action mydsl_action) {
        this.mydsl_action = mydsl_action;
    }

}