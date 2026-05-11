





import java.util.List;
import java.util.ArrayList;

public class tallerE1Java_Annotation  {

    private String content;
    private String type;





    private tallerE1Java_Attribute tallere1java_attribute;


    public tallerE1Java_Annotation(
        String content,        String type    ) {
        this.content = content;
        this.type = type;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public tallerE1Java_Attribute getTallere1java_attribute() {
        return tallere1java_attribute;
    }

    public void setTallere1java_attribute(tallerE1Java_Attribute tallere1java_attribute) {
        this.tallere1java_attribute = tallere1java_attribute;
    }

}