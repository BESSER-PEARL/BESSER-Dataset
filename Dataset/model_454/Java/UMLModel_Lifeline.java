





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Lifeline extends NamedElement {

    private String decomposedAs;
    private String represents;
    private String coveredBy;
    private String interaction;





    private UMLModel_ValueSpecification umlmodel_valuespecification;




    private UMLModel_Interaction umlmodel_interaction;


    public UMLModel_Lifeline(
        String decomposedAs,        String represents,        String coveredBy,        String interaction    ) {
        super(
        );
        this.decomposedAs = decomposedAs;
        this.represents = represents;
        this.coveredBy = coveredBy;
        this.interaction = interaction;
    }


    public String getDecomposedas() {
        return decomposedAs;
    }

    public void setDecomposedas(String decomposedAs) {
        this.decomposedAs = decomposedAs;
    }
    public String getRepresents() {
        return represents;
    }

    public void setRepresents(String represents) {
        this.represents = represents;
    }
    public String getCoveredby() {
        return coveredBy;
    }

    public void setCoveredby(String coveredBy) {
        this.coveredBy = coveredBy;
    }
    public String getInteraction() {
        return interaction;
    }

    public void setInteraction(String interaction) {
        this.interaction = interaction;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }
    public UMLModel_Interaction getUmlmodel_interaction() {
        return umlmodel_interaction;
    }

    public void setUmlmodel_interaction(UMLModel_Interaction umlmodel_interaction) {
        this.umlmodel_interaction = umlmodel_interaction;
    }

}