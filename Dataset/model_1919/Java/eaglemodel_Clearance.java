





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Clearance  {

    private int class_;
    private float value;





    private eaglemodel_Class eaglemodel_class;


    public eaglemodel_Clearance(
        int class_,        float value    ) {
        this.class_ = class_;
        this.value = value;
    }


    public int getClass_() {
        return class_;
    }

    public void setClass_(int class_) {
        this.class_ = class_;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public eaglemodel_Class getEaglemodel_class() {
        return eaglemodel_class;
    }

    public void setEaglemodel_class(eaglemodel_Class eaglemodel_class) {
        this.eaglemodel_class = eaglemodel_class;
    }

}