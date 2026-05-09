





import java.util.List;
import java.util.ArrayList;

public class project_WorkingHours extends ProjectAttribute, ResourceAttribute {

    private boolean off;





    private project_Shift project_shift;


    public project_WorkingHours(
        boolean off    ) {
        super(
        );
        this.off = off;
    }


    public boolean getOff() {
        return off;
    }

    public void setOff(boolean off) {
        this.off = off;
    }

    public project_Shift getProject_shift() {
        return project_shift;
    }

    public void setProject_shift(project_Shift project_shift) {
        this.project_shift = project_shift;
    }

}