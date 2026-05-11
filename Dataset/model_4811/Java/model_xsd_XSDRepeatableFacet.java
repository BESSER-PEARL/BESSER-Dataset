





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDRepeatableFacet extends XSDConstrainingFacet {






    private List<XSDAnnotation> xsdannotations;


    public model_xsd_XSDRepeatableFacet(
    ) {
        super(
        );
        this.xsdannotations = new ArrayList<>();
    }

    public model_xsd_XSDRepeatableFacet(
        ArrayList<XSDAnnotation> xsdannotations    ) {
        this.xsdannotations = xsdannotations;
    }


    public List<XSDAnnotation> getXsdannotations() {
        return xsdannotations;
    }

    public void addXsdannotation(Xsdannotation xsdannotation) {
        this.xsdannotations.add(xsdannotation);
    }

}