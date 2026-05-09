





import java.util.List;
import java.util.ArrayList;

public class presentation_SashForm extends Composite {

    private String group3;
    private String orientation;
    private String sashWidth1;
    private String sASHWIDTH;
    private String weights;



    public presentation_SashForm(
        String group3,        String orientation,        String sashWidth1,        String sASHWIDTH,        String weights    ) {
        super(
        );
        this.group3 = group3;
        this.orientation = orientation;
        this.sashWidth1 = sashWidth1;
        this.sASHWIDTH = sASHWIDTH;
        this.weights = weights;
    }


    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getSashwidth1() {
        return sashWidth1;
    }

    public void setSashwidth1(String sashWidth1) {
        this.sashWidth1 = sashWidth1;
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


}