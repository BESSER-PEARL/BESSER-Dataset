





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDAttributeUse extends xsd_XSDComponent, xsd_XSDAttributeGroupContent {

    private String use;
    private String lexicalValue;
    private boolean required;
    private String constraint;
    private String value;



    public model_xsd_XSDAttributeUse(
        String use,        String lexicalValue,        boolean required,        String constraint,        String value    ) {
        super(
        );
        this.use = use;
        this.lexicalValue = lexicalValue;
        this.required = required;
        this.constraint = constraint;
        this.value = value;
    }


    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }
    public String getLexicalvalue() {
        return lexicalValue;
    }

    public void setLexicalvalue(String lexicalValue) {
        this.lexicalValue = lexicalValue;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}