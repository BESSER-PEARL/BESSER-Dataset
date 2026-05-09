





import java.util.List;
import java.util.ArrayList;

public class presentation_Document  {

    private String mixed;





    private presentation_XMLDataProvider presentation_xmldataprovider;


    public presentation_Document(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public presentation_XMLDataProvider getPresentation_xmldataprovider() {
        return presentation_xmldataprovider;
    }

    public void setPresentation_xmldataprovider(presentation_XMLDataProvider presentation_xmldataprovider) {
        this.presentation_xmldataprovider = presentation_xmldataprovider;
    }

}