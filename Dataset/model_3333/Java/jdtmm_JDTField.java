





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTField extends JDTMember {

    private String final;
    private String isMultiValued;
    private String abstract;
    private String generateGetter;
    private String generateSetter;
    private String static;
    private String value;



    public jdtmm_JDTField(
        String final,        String isMultiValued,        String abstract,        String generateGetter,        String generateSetter,        String static,        String value    ) {
        super(
        );
        this.final = final;
        this.isMultiValued = isMultiValued;
        this.abstract = abstract;
        this.generateGetter = generateGetter;
        this.generateSetter = generateSetter;
        this.static = static;
        this.value = value;
    }


    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getIsmultivalued() {
        return isMultiValued;
    }

    public void setIsmultivalued(String isMultiValued) {
        this.isMultiValued = isMultiValued;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getGenerategetter() {
        return generateGetter;
    }

    public void setGenerategetter(String generateGetter) {
        this.generateGetter = generateGetter;
    }
    public String getGeneratesetter() {
        return generateSetter;
    }

    public void setGeneratesetter(String generateSetter) {
        this.generateSetter = generateSetter;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}