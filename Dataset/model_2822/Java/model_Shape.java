





import java.util.List;
import java.util.ArrayList;

public class model_Shape extends FontSupport, ColorAlphaSupport, IconPositionSupport, TextAlignmentSupport, LineStyleSupport, Widget, RotationSupport, IconSupport, BorderSupport, LinkSupport, SkinSupport, ColorBackgroundSupport, ColorForegroundSupport {

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