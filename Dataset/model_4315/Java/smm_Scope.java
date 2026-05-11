





import java.util.List;
import java.util.ArrayList;

public class smm_Scope extends AbstractMeasureElement {

    private String class_;





    private smm_Measure smm_measure;


    public smm_Scope(
        String class_    ) {
        super(
        );
        this.class_ = class_;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }

}