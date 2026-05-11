





import java.util.List;
import java.util.ArrayList;

public class persistence_Attribute extends Label, Feature {

    private boolean unique;
    private String ormType;
    private boolean hidden;
    private String placeholder;
    private String interfaceType;
    private String validationPattern;
    private String persistentType;
    private boolean containerUnique;
    private String inputColumnClass;
    private String inputElementClass;





    private persistence_Attribute persistence_attribute;




    private persistence_Entity persistence_entity;


    public persistence_Attribute(
        boolean unique,        String ormType,        boolean hidden,        String placeholder,        String interfaceType,        String validationPattern,        String persistentType,        boolean containerUnique,        String inputColumnClass,        String inputElementClass    ) {
        super(
        );
        this.unique = unique;
        this.ormType = ormType;
        this.hidden = hidden;
        this.placeholder = placeholder;
        this.interfaceType = interfaceType;
        this.validationPattern = validationPattern;
        this.persistentType = persistentType;
        this.containerUnique = containerUnique;
        this.inputColumnClass = inputColumnClass;
        this.inputElementClass = inputElementClass;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getOrmtype() {
        return ormType;
    }

    public void setOrmtype(String ormType) {
        this.ormType = ormType;
    }
    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }
    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public String getValidationpattern() {
        return validationPattern;
    }

    public void setValidationpattern(String validationPattern) {
        this.validationPattern = validationPattern;
    }
    public String getPersistenttype() {
        return persistentType;
    }

    public void setPersistenttype(String persistentType) {
        this.persistentType = persistentType;
    }
    public boolean getContainerunique() {
        return containerUnique;
    }

    public void setContainerunique(boolean containerUnique) {
        this.containerUnique = containerUnique;
    }
    public String getInputcolumnclass() {
        return inputColumnClass;
    }

    public void setInputcolumnclass(String inputColumnClass) {
        this.inputColumnClass = inputColumnClass;
    }
    public String getInputelementclass() {
        return inputElementClass;
    }

    public void setInputelementclass(String inputElementClass) {
        this.inputElementClass = inputElementClass;
    }

    public persistence_Attribute getPersistence_attribute() {
        return persistence_attribute;
    }

    public void setPersistence_attribute(persistence_Attribute persistence_attribute) {
        this.persistence_attribute = persistence_attribute;
    }
    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }

}