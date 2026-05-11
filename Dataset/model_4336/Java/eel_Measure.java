





import java.util.List;
import java.util.ArrayList;

public class eel_Measure  {

    private String targetClass;
    private String subname;
    private String name;
    private String targetOperation;





    private eel_Platform eel_platform;


    public eel_Measure(
        String targetClass,        String subname,        String name,        String targetOperation    ) {
        this.targetClass = targetClass;
        this.subname = subname;
        this.name = name;
        this.targetOperation = targetOperation;
    }


    public String getTargetclass() {
        return targetClass;
    }

    public void setTargetclass(String targetClass) {
        this.targetClass = targetClass;
    }
    public String getSubname() {
        return subname;
    }

    public void setSubname(String subname) {
        this.subname = subname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTargetoperation() {
        return targetOperation;
    }

    public void setTargetoperation(String targetOperation) {
        this.targetOperation = targetOperation;
    }

    public eel_Platform getEel_platform() {
        return eel_platform;
    }

    public void setEel_platform(eel_Platform eel_platform) {
        this.eel_platform = eel_platform;
    }

}