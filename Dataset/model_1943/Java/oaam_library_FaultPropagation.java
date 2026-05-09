





import java.util.List;
import java.util.ArrayList;

public class oaam_library_FaultPropagation extends OaamBaseElementA {

    private String outputState;



    public oaam_library_FaultPropagation(
        String outputState    ) {
        super(
        );
        this.outputState = outputState;
    }


    public String getOutputstate() {
        return outputState;
    }

    public void setOutputstate(String outputState) {
        this.outputState = outputState;
    }


}