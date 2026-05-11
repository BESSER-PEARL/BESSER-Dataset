





import java.util.List;
import java.util.ArrayList;

public class JavaMM_Annotation  {

    private String type;
    private String content;





    private JavaMM_Attribute javamm_attribute;


    public JavaMM_Annotation(
        String type,        String content    ) {
        this.type = type;
        this.content = content;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public JavaMM_Attribute getJavamm_attribute() {
        return javamm_attribute;
    }

    public void setJavamm_attribute(JavaMM_Attribute javamm_attribute) {
        this.javamm_attribute = javamm_attribute;
    }

}