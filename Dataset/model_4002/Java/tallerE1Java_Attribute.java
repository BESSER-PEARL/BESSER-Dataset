





import java.util.List;
import java.util.ArrayList;

public class tallerE1Java_Attribute  {

    private String visibility;
    private String name;





    private tallerE1Java_Class tallere1java_class;


    public tallerE1Java_Attribute(
        String visibility,        String name    ) {
        this.visibility = visibility;
        this.name = name;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tallerE1Java_Class getTallere1java_class() {
        return tallere1java_class;
    }

    public void setTallere1java_class(tallerE1Java_Class tallere1java_class) {
        this.tallere1java_class = tallere1java_class;
    }

}