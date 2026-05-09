





import java.util.List;
import java.util.ArrayList;

public class presentation_Canvas extends Composite {

    private String mixed1;
    private String group3;



    public presentation_Canvas(
        String mixed1,        String group3    ) {
        super(
        );
        this.mixed1 = mixed1;
        this.group3 = group3;
    }


    public String getMixed1() {
        return mixed1;
    }

    public void setMixed1(String mixed1) {
        this.mixed1 = mixed1;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }


}