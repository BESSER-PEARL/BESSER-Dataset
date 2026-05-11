





import java.util.List;
import java.util.ArrayList;

public class MARTE_RSM_Distribute extends Allocate {

    private String patternShape;
    private String fromTiler;
    private String toTiler;
    private String repetitionSpace;



    public MARTE_RSM_Distribute(
        String patternShape,        String fromTiler,        String toTiler,        String repetitionSpace    ) {
        super(
        );
        this.patternShape = patternShape;
        this.fromTiler = fromTiler;
        this.toTiler = toTiler;
        this.repetitionSpace = repetitionSpace;
    }


    public String getPatternshape() {
        return patternShape;
    }

    public void setPatternshape(String patternShape) {
        this.patternShape = patternShape;
    }
    public String getFromtiler() {
        return fromTiler;
    }

    public void setFromtiler(String fromTiler) {
        this.fromTiler = fromTiler;
    }
    public String getTotiler() {
        return toTiler;
    }

    public void setTotiler(String toTiler) {
        this.toTiler = toTiler;
    }
    public String getRepetitionspace() {
        return repetitionSpace;
    }

    public void setRepetitionspace(String repetitionSpace) {
        this.repetitionSpace = repetitionSpace;
    }


}