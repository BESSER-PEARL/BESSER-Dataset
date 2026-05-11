





import java.util.List;
import java.util.ArrayList;

public class yuml_Method extends ClassMember {

    private String arguments;





    private yuml_Class yuml_class;


    public yuml_Method(
        String arguments    ) {
        super(
        );
        this.arguments = arguments;
    }


    public String getArguments() {
        return arguments;
    }

    public void setArguments(String arguments) {
        this.arguments = arguments;
    }

    public yuml_Class getYuml_class() {
        return yuml_class;
    }

    public void setYuml_class(yuml_Class yuml_class) {
        this.yuml_class = yuml_class;
    }

}