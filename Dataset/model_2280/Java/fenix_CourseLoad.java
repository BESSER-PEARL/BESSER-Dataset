





import java.util.List;
import java.util.ArrayList;

public class fenix_CourseLoad  {

    private String id;
    private String type;
    private int totalQuantity;
    private int unitQuantity;
    private String name;
    private String description;





    private fenix_CourseLoad fenix_courseload;




    private fenix_Shift fenix_shift;




    private fenix_LessonPeriod fenix_lessonperiod;


    public fenix_CourseLoad(
        String id,        String type,        int totalQuantity,        int unitQuantity,        String name,        String description    ) {
        this.id = id;
        this.type = type;
        this.totalQuantity = totalQuantity;
        this.unitQuantity = unitQuantity;
        this.name = name;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getTotalquantity() {
        return totalQuantity;
    }

    public void setTotalquantity(int totalQuantity) {
        this.totalQuantity = totalQuantity;
    }
    public int getUnitquantity() {
        return unitQuantity;
    }

    public void setUnitquantity(int unitQuantity) {
        this.unitQuantity = unitQuantity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public fenix_CourseLoad getFenix_courseload() {
        return fenix_courseload;
    }

    public void setFenix_courseload(fenix_CourseLoad fenix_courseload) {
        this.fenix_courseload = fenix_courseload;
    }
    public fenix_Shift getFenix_shift() {
        return fenix_shift;
    }

    public void setFenix_shift(fenix_Shift fenix_shift) {
        this.fenix_shift = fenix_shift;
    }
    public fenix_LessonPeriod getFenix_lessonperiod() {
        return fenix_lessonperiod;
    }

    public void setFenix_lessonperiod(fenix_LessonPeriod fenix_lessonperiod) {
        this.fenix_lessonperiod = fenix_lessonperiod;
    }

}