





import java.util.List;
import java.util.ArrayList;

public class jointPackage_HSM2FSM_SrcAbstractState  {

    private String name;





    private SrcStateMachine srcstatemachine;


    public jointPackage_HSM2FSM_SrcAbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SrcStateMachine getSrcstatemachine() {
        return srcstatemachine;
    }

    public void setSrcstatemachine(SrcStateMachine srcstatemachine) {
        this.srcstatemachine = srcstatemachine;
    }

}