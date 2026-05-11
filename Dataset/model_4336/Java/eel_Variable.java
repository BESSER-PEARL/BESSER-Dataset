





import java.util.List;
import java.util.ArrayList;

public class eel_Variable  {

    private String name;
    private String vibility;
    private String value;





    private eel_Platform eel_platform;


    public eel_Variable(
        String name,        String vibility,        String value    ) {
        this.name = name;
        this.vibility = vibility;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVibility() {
        return vibility;
    }

    public void setVibility(String vibility) {
        this.vibility = vibility;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public eel_Platform getEel_platform() {
        return eel_platform;
    }

    public void setEel_platform(eel_Platform eel_platform) {
        this.eel_platform = eel_platform;
    }

}