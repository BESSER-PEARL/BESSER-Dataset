





import java.util.List;
import java.util.ArrayList;

public class dsl_Dropfile extends Action {

    private String target;



    public dsl_Dropfile(
        String target    ) {
        super(
        );
        this.target = target;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}