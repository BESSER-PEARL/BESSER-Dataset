





import java.util.List;
import java.util.ArrayList;

public class cal_AstAnnotationArgument  {

    private String name;
    private String value;





    private cal_AstAnnotation cal_astannotation;


    public cal_AstAnnotationArgument(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public cal_AstAnnotation getCal_astannotation() {
        return cal_astannotation;
    }

    public void setCal_astannotation(cal_AstAnnotation cal_astannotation) {
        this.cal_astannotation = cal_astannotation;
    }

}