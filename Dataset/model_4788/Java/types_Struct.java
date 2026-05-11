





import java.util.List;
import java.util.ArrayList;

public class types_Struct extends Type {

    private boolean isDcpsDataType;
    private String name;





    private List<types_Field> types_fields;




    private List<types_Key> types_keys;


    public types_Struct(
        boolean isDcpsDataType,        String name    ) {
        super(
        );
        this.isDcpsDataType = isDcpsDataType;
        this.name = name;
        this.types_fields = new ArrayList<>();
        this.types_keys = new ArrayList<>();
    }

    public types_Struct(
        boolean isDcpsDataType,        String name        ArrayList<types_Field> types_fields,        ArrayList<types_Key> types_keys    ) {
        this.isDcpsDataType = isDcpsDataType;
        this.name = name;
        this.types_fields = types_fields;
        this.types_keys = types_keys;
    }

    public boolean getIsdcpsdatatype() {
        return isDcpsDataType;
    }

    public void setIsdcpsdatatype(boolean isDcpsDataType) {
        this.isDcpsDataType = isDcpsDataType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<types_Field> getTypes_fields() {
        return types_fields;
    }

    public void addTypes_field(Types_field types_field) {
        this.types_fields.add(types_field);
    }
    public List<types_Key> getTypes_keys() {
        return types_keys;
    }

    public void addTypes_key(Types_key types_key) {
        this.types_keys.add(types_key);
    }

}