





import java.util.List;
import java.util.ArrayList;

public class lecturer  {

    private String module;





    private Staff staff;


    public lecturer(
        String module    ) {
        this.module = module;
    }


    public String getModule() {
        return module;
    }

    public void setModule(String module) {
        this.module = module;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}