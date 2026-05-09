





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_DestroyObjectAction extends Action {

    private boolean destroyLinks;
    private boolean destroyOwnedObjects;





    private BasicActions_InputPin basicactions_inputpin;


    public xmof_IntermediateActions_DestroyObjectAction(
        boolean destroyLinks,        boolean destroyOwnedObjects    ) {
        super(
        );
        this.destroyLinks = destroyLinks;
        this.destroyOwnedObjects = destroyOwnedObjects;
    }


    public boolean getDestroylinks() {
        return destroyLinks;
    }

    public void setDestroylinks(boolean destroyLinks) {
        this.destroyLinks = destroyLinks;
    }
    public boolean getDestroyownedobjects() {
        return destroyOwnedObjects;
    }

    public void setDestroyownedobjects(boolean destroyOwnedObjects) {
        this.destroyOwnedObjects = destroyOwnedObjects;
    }

    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}