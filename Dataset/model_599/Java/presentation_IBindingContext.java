





import java.util.List;
import java.util.ArrayList;

public class presentation_IBindingContext  {

    private String mixed;





    private presentation_AbstractDataProvider presentation_abstractdataprovider;


    public presentation_IBindingContext(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_AbstractDataProvider getPresentation_abstractdataprovider() {
        return presentation_abstractdataprovider;
    }

    public void setPresentation_abstractdataprovider(presentation_AbstractDataProvider presentation_abstractdataprovider) {
        this.presentation_abstractdataprovider = presentation_abstractdataprovider;
    }

}