





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends SkinSupport, TextAlignmentSupport, RotationSupport, LineStyleSupport, LinkSupport, BorderSupport, IconPositionSupport, ColorBackgroundSupport, Widget, FontSupport, ColorAlphaSupport, ColorForegroundSupport, IconSupport {

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