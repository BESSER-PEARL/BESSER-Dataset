





import java.util.List;
import java.util.ArrayList;

public class uml_LinkEndDestructionData extends LinkEndData {

    private String isDestroyDuplicates;





    private uml_InputPin uml_inputpin;


    public uml_LinkEndDestructionData(
        String isDestroyDuplicates    ) {
        super(
        );
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


    public String getIsdestroyduplicates() {
        return isDestroyDuplicates;
    }

    public void setIsdestroyduplicates(String isDestroyDuplicates) {
        this.isDestroyDuplicates = isDestroyDuplicates;
    }

    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}