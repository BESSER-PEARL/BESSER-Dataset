





import java.util.List;
import java.util.ArrayList;

public class cal_AstAnnotationArgument  {

    private String value;
    private String name;





    private cal_AstAnnotation cal_astannotation;


    public cal_AstAnnotationArgument(
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

    public cal_AstAnnotation getCal_astannotation() {
        return cal_astannotation;
    }

    public void setCal_astannotation(cal_AstAnnotation cal_astannotation) {
        this.cal_astannotation = cal_astannotation;
    }

}