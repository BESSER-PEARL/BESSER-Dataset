





import java.util.List;
import java.util.ArrayList;

public class UML_14_Generalization extends Relationship {

    private String discriminator;





    private UML_14_GeneralizableElement uml_14_generalizableelement;




    private List<UML_14_GeneralizableElement> uml_14_generalizableelements;




    private UML_14_GeneralizableElement uml_14_generalizableelement;




    private List<UML_14_GeneralizableElement> uml_14_generalizableelements;


    public UML_14_Generalization(
        String discriminator    ) {
        super(
        );
        this.discriminator = discriminator;
        this.uml_14_generalizableelements = new ArrayList<>();
        this.uml_14_generalizableelements = new ArrayList<>();
    }

    public UML_14_Generalization(
        String discriminator        ArrayList<UML_14_GeneralizableElement> uml_14_generalizableelements,        ArrayList<UML_14_GeneralizableElement> uml_14_generalizableelements    ) {
        this.discriminator = discriminator;
        this.uml_14_generalizableelements = uml_14_generalizableelements;
        this.uml_14_generalizableelements = uml_14_generalizableelements;
    }

    public String getDiscriminator() {
        return discriminator;
    }

    public void setDiscriminator(String discriminator) {
        this.discriminator = discriminator;
    }

    public UML_14_GeneralizableElement getUml_14_generalizableelement() {
        return uml_14_generalizableelement;
    }

    public void setUml_14_generalizableelement(UML_14_GeneralizableElement uml_14_generalizableelement) {
        this.uml_14_generalizableelement = uml_14_generalizableelement;
    }
    public List<UML_14_GeneralizableElement> getUml_14_generalizableelements() {
        return uml_14_generalizableelements;
    }

    public void addUml_14_generalizableelement(Uml_14_generalizableelement uml_14_generalizableelement) {
        this.uml_14_generalizableelements.add(uml_14_generalizableelement);
    }
    public UML_14_GeneralizableElement getUml_14_generalizableelement() {
        return uml_14_generalizableelement;
    }

    public void setUml_14_generalizableelement(UML_14_GeneralizableElement uml_14_generalizableelement) {
        this.uml_14_generalizableelement = uml_14_generalizableelement;
    }
    public List<UML_14_GeneralizableElement> getUml_14_generalizableelements() {
        return uml_14_generalizableelements;
    }

    public void addUml_14_generalizableelement(Uml_14_generalizableelement uml_14_generalizableelement) {
        this.uml_14_generalizableelements.add(uml_14_generalizableelement);
    }

}