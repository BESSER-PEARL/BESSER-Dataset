





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends IconSupport, IconPositionSupport, ColorAlphaSupport, SkinSupport, RotationSupport, LineStyleSupport, Widget, BorderSupport, ColorBackgroundSupport, TextAlignmentSupport, LinkSupport, FontSupport, ColorForegroundSupport {

    private String shapeType;



    public model_Shape(
        String shapeType    ) {
        super(
        );
        this.shapeType = shapeType;
    }


    public String getShapetype() {
        return shapeType;
    }

    public void setShapetype(String shapeType) {
        this.shapeType = shapeType;
    }


}