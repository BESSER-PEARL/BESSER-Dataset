





import java.util.List;
import java.util.ArrayList;

public class dom_Attribute extends ReferenceableByXmadslVariable, QueryParameterReference, PresentableFeature, IDocumentable {

    private boolean derived;
    private String defaultValue;
    private boolean composition;
    private String dataTypeName;
    private boolean version;
    private boolean required;
    private boolean identifier;
    private boolean many;
    private boolean reference;
    private boolean transient;
    private boolean readOnly;





    private dom_Entity dom_entity;




    private dom_Attribute dom_attribute;




    private dom_Entity dom_entity;




    private dom_Attribute dom_attribute;




    private dom_Attribute dom_attribute;




    private dom_Entity dom_entity;




    private dom_Entity dom_entity;


    public dom_Attribute(
        boolean derived,        String defaultValue,        boolean composition,        String dataTypeName,        boolean version,        boolean required,        boolean identifier,        boolean many,        boolean reference,        boolean transient,        boolean readOnly    ) {
        super(
        );
        this.derived = derived;
        this.defaultValue = defaultValue;
        this.composition = composition;
        this.dataTypeName = dataTypeName;
        this.version = version;
        this.required = required;
        this.identifier = identifier;
        this.many = many;
        this.reference = reference;
        this.transient = transient;
        this.readOnly = readOnly;
    }


    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getComposition() {
        return composition;
    }

    public void setComposition(boolean composition) {
        this.composition = composition;
    }
    public String getDatatypename() {
        return dataTypeName;
    }

    public void setDatatypename(String dataTypeName) {
        this.dataTypeName = dataTypeName;
    }
    public boolean getVersion() {
        return version;
    }

    public void setVersion(boolean version) {
        this.version = version;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public boolean getIdentifier() {
        return identifier;
    }

    public void setIdentifier(boolean identifier) {
        this.identifier = identifier;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getReference() {
        return reference;
    }

    public void setReference(boolean reference) {
        this.reference = reference;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }
    public dom_Entity getDom_entity() {
        return dom_entity;
    }

    public void setDom_entity(dom_Entity dom_entity) {
        this.dom_entity = dom_entity;
    }

}