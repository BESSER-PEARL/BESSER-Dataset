





import java.util.List;
import java.util.ArrayList;

public class MARTE_RSM_Reshape extends LinkTopology {

    private String patternShape;
    private String repetitonShape;



    public MARTE_RSM_Reshape(
        String patternShape,        String repetitonShape    ) {
        super(
        );
        this.patternShape = patternShape;
        this.repetitonShape = repetitonShape;
    }


    public String getPatternshape() {
        return patternShape;
    }

    public void setPatternshape(String patternShape) {
        this.patternShape = patternShape;
    }
    public String getRepetitonshape() {
        return repetitonShape;
    }

    public void setRepetitonshape(String repetitonShape) {
        this.repetitonShape = repetitonShape;
    }


}