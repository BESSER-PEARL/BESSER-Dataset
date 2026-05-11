





import java.util.List;
import java.util.ArrayList;

public class aadl2_ProcessorCall extends CallSpecification {

    private String subprogramAccessName;



    public aadl2_ProcessorCall(
        String subprogramAccessName    ) {
        super(
        );
        this.subprogramAccessName = subprogramAccessName;
    }


    public String getSubprogramaccessname() {
        return subprogramAccessName;
    }

    public void setSubprogramaccessname(String subprogramAccessName) {
        this.subprogramAccessName = subprogramAccessName;
    }


}