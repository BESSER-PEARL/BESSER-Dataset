





import java.util.List;
import java.util.ArrayList;

public class coCoMM_OptimizationCC extends ConfigurationConstraint {

    private String funct;



    public coCoMM_OptimizationCC(
        String funct    ) {
        super(
        );
        this.funct = funct;
    }


    public String getFunct() {
        return funct;
    }

    public void setFunct(String funct) {
        this.funct = funct;
    }


}