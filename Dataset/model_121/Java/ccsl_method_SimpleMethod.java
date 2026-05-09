





import java.util.List;
import java.util.ArrayList;

public class ccsl_method_SimpleMethod extends elements_Element, annotation_AnnotableElement {

    private String paramsKind;
    private String visibility;



    public ccsl_method_SimpleMethod(
        String paramsKind,        String visibility    ) {
        super(
        );
        this.paramsKind = paramsKind;
        this.visibility = visibility;
    }


    public String getParamskind() {
        return paramsKind;
    }

    public void setParamskind(String paramsKind) {
        this.paramsKind = paramsKind;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}