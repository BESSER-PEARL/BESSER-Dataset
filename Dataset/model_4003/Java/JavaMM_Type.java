





import java.util.List;
import java.util.ArrayList;

public class JavaMM_Type  {

    private String name;





    private JavaMM_Attribute javamm_attribute;


    public JavaMM_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public JavaMM_Attribute getJavamm_attribute() {
        return javamm_attribute;
    }

    public void setJavamm_attribute(JavaMM_Attribute javamm_attribute) {
        this.javamm_attribute = javamm_attribute;
    }

}