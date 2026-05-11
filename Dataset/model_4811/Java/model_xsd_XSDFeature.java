





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDFeature extends XSDNamedComponent {

    private boolean featureReference;
    private String constraint;
    private String lexicalValue;
    private String form;
    private boolean global_;
    private String value;





    private XSDScope xsdscope;




    private XSDTypeDefinition xsdtypedefinition;




    private XSDFeature xsdfeature;


    public model_xsd_XSDFeature(
        boolean featureReference,        String constraint,        String lexicalValue,        String form,        boolean global_,        String value    ) {
        super(
        );
        this.featureReference = featureReference;
        this.constraint = constraint;
        this.lexicalValue = lexicalValue;
        this.form = form;
        this.global_ = global_;
        this.value = value;
    }


    public boolean getFeaturereference() {
        return featureReference;
    }

    public void setFeaturereference(boolean featureReference) {
        this.featureReference = featureReference;
    }
    public String getConstraint() {
        return constraint;
    }

    public void setConstraint(String constraint) {
        this.constraint = constraint;
    }
    public String getLexicalvalue() {
        return lexicalValue;
    }

    public void setLexicalvalue(String lexicalValue) {
        this.lexicalValue = lexicalValue;
    }
    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }
    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public XSDScope getXsdscope() {
        return xsdscope;
    }

    public void setXsdscope(XSDScope xsdscope) {
        this.xsdscope = xsdscope;
    }
    public XSDTypeDefinition getXsdtypedefinition() {
        return xsdtypedefinition;
    }

    public void setXsdtypedefinition(XSDTypeDefinition xsdtypedefinition) {
        this.xsdtypedefinition = xsdtypedefinition;
    }
    public XSDFeature getXsdfeature() {
        return xsdfeature;
    }

    public void setXsdfeature(XSDFeature xsdfeature) {
        this.xsdfeature = xsdfeature;
    }

}