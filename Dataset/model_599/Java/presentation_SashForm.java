





import java.util.List;
import java.util.ArrayList;

public class presentation_SashForm extends Composite {

    private String orientation;
    private String group3;
    private String sASHWIDTH;
    private String weights;
    private String sashWidth1;



    public presentation_SashForm(
        String orientation,        String group3,        String sASHWIDTH,        String weights,        String sashWidth1    ) {
        super(
        );
        this.orientation = orientation;
        this.group3 = group3;
        this.sASHWIDTH = sASHWIDTH;
        this.weights = weights;
        this.sashWidth1 = sashWidth1;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getSashwidth() {
        return sASHWIDTH;
    }

    public void setSashwidth(String sASHWIDTH) {
        this.sASHWIDTH = sASHWIDTH;
    }
    public String getWeights() {
        return weights;
    }

    public void setWeights(String weights) {
        this.weights = weights;
    }
    public String getSashwidth1() {
        return sashWidth1;
    }

    public void setSashwidth1(String sashWidth1) {
        this.sashWidth1 = sashWidth1;
    }


}