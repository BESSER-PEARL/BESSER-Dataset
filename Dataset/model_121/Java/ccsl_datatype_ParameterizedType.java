





import java.util.List;
import java.util.ArrayList;

public class ccsl_datatype_ParameterizedType extends ObjectType {






    private complexType_DeclaredType complextype_declaredtype;




    private List<datatype_ObjectType> datatype_objecttypes;


    public ccsl_datatype_ParameterizedType(
    ) {
        super(
        );
        this.datatype_objecttypes = new ArrayList<>();
    }

    public ccsl_datatype_ParameterizedType(
        ArrayList<datatype_ObjectType> datatype_objecttypes    ) {
        this.datatype_objecttypes = datatype_objecttypes;
    }


    public complexType_DeclaredType getComplextype_declaredtype() {
        return complextype_declaredtype;
    }

    public void setComplextype_declaredtype(complexType_DeclaredType complextype_declaredtype) {
        this.complextype_declaredtype = complextype_declaredtype;
    }
    public List<datatype_ObjectType> getDatatype_objecttypes() {
        return datatype_objecttypes;
    }

    public void addDatatype_objecttype(Datatype_objecttype datatype_objecttype) {
        this.datatype_objecttypes.add(datatype_objecttype);
    }

}