





import java.util.List;
import java.util.ArrayList;

public class cal_AstAnnotation  {

    private String name;





    private cal_AstEntity cal_astentity;


    public cal_AstAnnotation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstEntity getCal_astentity() {
        return cal_astentity;
    }

    public void setCal_astentity(cal_AstEntity cal_astentity) {
        this.cal_astentity = cal_astentity;
    }

}