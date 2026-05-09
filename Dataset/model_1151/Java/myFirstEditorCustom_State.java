





import java.util.List;
import java.util.ArrayList;

public class myFirstEditorCustom_State  {

    private String name;
    private String type;





    private myFirstEditorCustom_StateMachine myfirsteditorcustom_statemachine;


    public myFirstEditorCustom_State(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public myFirstEditorCustom_StateMachine getMyfirsteditorcustom_statemachine() {
        return myfirsteditorcustom_statemachine;
    }

    public void setMyfirsteditorcustom_statemachine(myFirstEditorCustom_StateMachine myfirsteditorcustom_statemachine) {
        this.myfirsteditorcustom_statemachine = myfirsteditorcustom_statemachine;
    }

}