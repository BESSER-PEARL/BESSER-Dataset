





import java.util.List;
import java.util.ArrayList;

public class fuml_IntermediateActions_LinkEndDestructionData extends LinkEndData {

    private boolean destroyDuplicates;





    private BasicActions_InputPin basicactions_inputpin;


    public fuml_IntermediateActions_LinkEndDestructionData(
        boolean destroyDuplicates    ) {
        super(
        );
        this.destroyDuplicates = destroyDuplicates;
    }


    public boolean getDestroyduplicates() {
        return destroyDuplicates;
    }

    public void setDestroyduplicates(boolean destroyDuplicates) {
        this.destroyDuplicates = destroyDuplicates;
    }

    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}