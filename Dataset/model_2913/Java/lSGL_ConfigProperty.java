





import java.util.List;
import java.util.ArrayList;

public class lSGL_ConfigProperty  {

    private String value;
    private String name;





    private lSGL_Generator lsgl_generator;


    public lSGL_ConfigProperty(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lSGL_Generator getLsgl_generator() {
        return lsgl_generator;
    }

    public void setLsgl_generator(lSGL_Generator lsgl_generator) {
        this.lsgl_generator = lsgl_generator;
    }

}