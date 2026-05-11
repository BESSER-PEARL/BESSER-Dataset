





import java.util.List;
import java.util.ArrayList;

public class smm_Operation extends AbstractMeasureElement {

    private String body;
    private String language;





    private smm_Measure smm_measure;




    private smm_MeasureRelationship smm_measurerelationship;




    private smm_Scope smm_scope;




    private smm_Scope smm_scope;


    public smm_Operation(
        String body,        String language    ) {
        super(
        );
        this.body = body;
        this.language = language;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public smm_MeasureRelationship getSmm_measurerelationship() {
        return smm_measurerelationship;
    }

    public void setSmm_measurerelationship(smm_MeasureRelationship smm_measurerelationship) {
        this.smm_measurerelationship = smm_measurerelationship;
    }
    public smm_Scope getSmm_scope() {
        return smm_scope;
    }

    public void setSmm_scope(smm_Scope smm_scope) {
        this.smm_scope = smm_scope;
    }
    public smm_Scope getSmm_scope() {
        return smm_scope;
    }

    public void setSmm_scope(smm_Scope smm_scope) {
        this.smm_scope = smm_scope;
    }

}