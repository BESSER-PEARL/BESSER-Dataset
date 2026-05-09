





import java.util.List;
import java.util.ArrayList;

public class presentation_Canvas extends Composite {

    private String group3;
    private String mixed1;



    public presentation_Canvas(
        String group3,        String mixed1    ) {
        super(
        );
        this.group3 = group3;
        this.mixed1 = mixed1;
    }


    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getMixed1() {
        return mixed1;
    }

    public void setMixed1(String mixed1) {
        this.mixed1 = mixed1;
    }


}