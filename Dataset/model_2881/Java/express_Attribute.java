





import java.util.List;
import java.util.ArrayList;

public class express_Attribute  {

    private String name;
    private String qualifier;
    private String expression;
    private boolean self;
    private boolean optional;





    private express_Entity express_entity;




    private express_Attribute express_attribute;




    private express_DataType express_datatype;




    private express_CollectionType express_collectiontype;




    private express_CollectionType express_collectiontype;


    public express_Attribute(
        String name,        String qualifier,        String expression,        boolean self,        boolean optional    ) {
        this.name = name;
        this.qualifier = qualifier;
        this.expression = expression;
        this.self = self;
        this.optional = optional;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public boolean getSelf() {
        return self;
    }

    public void setSelf(boolean self) {
        this.self = self;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }

    public express_Entity getExpress_entity() {
        return express_entity;
    }

    public void setExpress_entity(express_Entity express_entity) {
        this.express_entity = express_entity;
    }
    public express_Attribute getExpress_attribute() {
        return express_attribute;
    }

    public void setExpress_attribute(express_Attribute express_attribute) {
        this.express_attribute = express_attribute;
    }
    public express_DataType getExpress_datatype() {
        return express_datatype;
    }

    public void setExpress_datatype(express_DataType express_datatype) {
        this.express_datatype = express_datatype;
    }
    public express_CollectionType getExpress_collectiontype() {
        return express_collectiontype;
    }

    public void setExpress_collectiontype(express_CollectionType express_collectiontype) {
        this.express_collectiontype = express_collectiontype;
    }
    public express_CollectionType getExpress_collectiontype() {
        return express_collectiontype;
    }

    public void setExpress_collectiontype(express_CollectionType express_collectiontype) {
        this.express_collectiontype = express_collectiontype;
    }

}