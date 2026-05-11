





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_ExternalAttributeCalculationCall extends AttributeCalculation {

    private String qualifiedName;
    private String id;





    private trnetvisual_AttributePattern trnetvisual_attributepattern;




    private trnetvisual_AttributePattern trnetvisual_attributepattern;


    public trnetvisual_ExternalAttributeCalculationCall(
        String qualifiedName,        String id    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.id = id;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public trnetvisual_AttributePattern getTrnetvisual_attributepattern() {
        return trnetvisual_attributepattern;
    }

    public void setTrnetvisual_attributepattern(trnetvisual_AttributePattern trnetvisual_attributepattern) {
        this.trnetvisual_attributepattern = trnetvisual_attributepattern;
    }
    public trnetvisual_AttributePattern getTrnetvisual_attributepattern() {
        return trnetvisual_attributepattern;
    }

    public void setTrnetvisual_attributepattern(trnetvisual_AttributePattern trnetvisual_attributepattern) {
        this.trnetvisual_attributepattern = trnetvisual_attributepattern;
    }

}