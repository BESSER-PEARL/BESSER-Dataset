





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Generalization extends DirectedRelationship {

    private String specific;
    private String generalizationSet;
    private String general;
    private String isSubstitutable;



    public UMLModel_Generalization(
        String specific,        String generalizationSet,        String general,        String isSubstitutable    ) {
        super(
        );
        this.specific = specific;
        this.generalizationSet = generalizationSet;
        this.general = general;
        this.isSubstitutable = isSubstitutable;
    }


    public String getSpecific() {
        return specific;
    }

    public void setSpecific(String specific) {
        this.specific = specific;
    }
    public String getGeneralizationset() {
        return generalizationSet;
    }

    public void setGeneralizationset(String generalizationSet) {
        this.generalizationSet = generalizationSet;
    }
    public String getGeneral() {
        return general;
    }

    public void setGeneral(String general) {
        this.general = general;
    }
    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }


}