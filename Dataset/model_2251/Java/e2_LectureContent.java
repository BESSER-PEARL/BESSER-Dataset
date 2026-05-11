





import java.util.List;
import java.util.ArrayList;

public class e2_LectureContent  {

    private String Material;
    private String Type;





    private e2_Lecture e2_lecture;


    public e2_LectureContent(
        String Material,        String Type    ) {
        this.Material = Material;
        this.Type = Type;
    }


    public String getMaterial() {
        return Material;
    }

    public void setMaterial(String Material) {
        this.Material = Material;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public e2_Lecture getE2_lecture() {
        return e2_lecture;
    }

    public void setE2_lecture(e2_Lecture e2_lecture) {
        this.e2_lecture = e2_lecture;
    }

}