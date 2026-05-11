





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_entitymodel_Attribute  {

    private String attributeType;
    private String type;
    private String name;
    private String value;
    private boolean visible;





    private List<ElementoRealizacionVisibleAttribute> elementorealizacionvisibleattributes;




    private List<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes;




    private Entity entity;


    public gestionmodelosconsultas_entitymodel_Attribute(
        String attributeType,        String type,        String name,        String value,        boolean visible    ) {
        this.attributeType = attributeType;
        this.type = type;
        this.name = name;
        this.value = value;
        this.visible = visible;
        this.elementorealizacionvisibleattributes = new ArrayList<>();
        this.elementorealizacionvalueattributes = new ArrayList<>();
    }

    public gestionmodelosconsultas_entitymodel_Attribute(
        String attributeType,        String type,        String name,        String value,        boolean visible        ArrayList<ElementoRealizacionVisibleAttribute> elementorealizacionvisibleattributes,        ArrayList<ElementoRealizacionValueAttribute> elementorealizacionvalueattributes    ) {
        this.attributeType = attributeType;
        this.type = type;
        this.name = name;
        this.value = value;
        this.visible = visible;
        this.elementorealizacionvisibleattributes = elementorealizacionvisibleattributes;
        this.elementorealizacionvalueattributes = elementorealizacionvalueattributes;
    }

    public String getAttributetype() {
        return attributeType;
    }

    public void setAttributetype(String attributeType) {
        this.attributeType = attributeType;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public List<ElementoRealizacionVisibleAttribute> getElementorealizacionvisibleattributes() {
        return elementorealizacionvisibleattributes;
    }

    public void addElementorealizacionvisibleattribute(Elementorealizacionvisibleattribute elementorealizacionvisibleattribute) {
        this.elementorealizacionvisibleattributes.add(elementorealizacionvisibleattribute);
    }
    public List<ElementoRealizacionValueAttribute> getElementorealizacionvalueattributes() {
        return elementorealizacionvalueattributes;
    }

    public void addElementorealizacionvalueattribute(Elementorealizacionvalueattribute elementorealizacionvalueattribute) {
        this.elementorealizacionvalueattributes.add(elementorealizacionvalueattribute);
    }
    public Entity getEntity() {
        return entity;
    }

    public void setEntity(Entity entity) {
        this.entity = entity;
    }

}