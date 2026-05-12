





import java.util.List;
import java.util.ArrayList;

public class presentation_DimType  {

    private String shapeId;
    private String color;





    private presentation_SoundType presentation_soundtype;


    public presentation_DimType(
        String shapeId,        String color    ) {
        this.shapeId = shapeId;
        this.color = color;
    }


    public String getShapeid() {
        return shapeId;
    }

    public void setShapeid(String shapeId) {
        this.shapeId = shapeId;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public presentation_SoundType getPresentation_soundtype() {
        return presentation_soundtype;
    }

    public void setPresentation_soundtype(presentation_SoundType presentation_soundtype) {
        this.presentation_soundtype = presentation_soundtype;
    }

}