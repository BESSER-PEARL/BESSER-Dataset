





import java.util.List;
import java.util.ArrayList;

public class metamodel_Feature  {

    private boolean xmltransient;
    private String name;
    private boolean nullable;





    private metamodel_AssociationEntity metamodel_associationentity;




    private metamodel_Entity metamodel_entity;


    public metamodel_Feature(
        boolean xmltransient,        String name,        boolean nullable    ) {
        this.xmltransient = xmltransient;
        this.name = name;
        this.nullable = nullable;
    }


    public boolean getXmltransient() {
        return xmltransient;
    }

    public void setXmltransient(boolean xmltransient) {
        this.xmltransient = xmltransient;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public metamodel_AssociationEntity getMetamodel_associationentity() {
        return metamodel_associationentity;
    }

    public void setMetamodel_associationentity(metamodel_AssociationEntity metamodel_associationentity) {
        this.metamodel_associationentity = metamodel_associationentity;
    }
    public metamodel_Entity getMetamodel_entity() {
        return metamodel_entity;
    }

    public void setMetamodel_entity(metamodel_Entity metamodel_entity) {
        this.metamodel_entity = metamodel_entity;
    }

}