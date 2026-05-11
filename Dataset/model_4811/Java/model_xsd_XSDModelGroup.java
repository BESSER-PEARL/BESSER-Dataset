





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDModelGroup extends XSDTerm {

    private String compositor;





    private List<XSDParticle> xsdparticles;




    private List<XSDParticle> xsdparticles;




    private XSDAnnotation xsdannotation;


    public model_xsd_XSDModelGroup(
        String compositor    ) {
        super(
        );
        this.compositor = compositor;
        this.xsdparticles = new ArrayList<>();
        this.xsdparticles = new ArrayList<>();
    }

    public model_xsd_XSDModelGroup(
        String compositor        ArrayList<XSDParticle> xsdparticles,        ArrayList<XSDParticle> xsdparticles    ) {
        this.compositor = compositor;
        this.xsdparticles = xsdparticles;
        this.xsdparticles = xsdparticles;
    }

    public String getCompositor() {
        return compositor;
    }

    public void setCompositor(String compositor) {
        this.compositor = compositor;
    }

    public List<XSDParticle> getXsdparticles() {
        return xsdparticles;
    }

    public void addXsdparticle(Xsdparticle xsdparticle) {
        this.xsdparticles.add(xsdparticle);
    }
    public List<XSDParticle> getXsdparticles() {
        return xsdparticles;
    }

    public void addXsdparticle(Xsdparticle xsdparticle) {
        this.xsdparticles.add(xsdparticle);
    }
    public XSDAnnotation getXsdannotation() {
        return xsdannotation;
    }

    public void setXsdannotation(XSDAnnotation xsdannotation) {
        this.xsdannotation = xsdannotation;
    }

}