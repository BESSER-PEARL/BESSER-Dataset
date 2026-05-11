





import java.util.List;
import java.util.ArrayList;

public class e2_LectureContent  {

    private String Type;
    private String Material;



    public e2_LectureContent(
        String Type,        String Material    ) {
        this.Type = Type;
        this.Material = Material;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getMaterial() {
        return Material;
    }

    public void setMaterial(String Material) {
        this.Material = Material;
    }


}