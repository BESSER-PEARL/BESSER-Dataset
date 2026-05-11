





import java.util.List;
import java.util.ArrayList;

public class jsonldConverter_Property  {

    private boolean one;
    private boolean many;
    private String name;





    private jsonldConverter_Type jsonldconverter_type;




    private jsonldConverter_Entity jsonldconverter_entity;


    public jsonldConverter_Property(
        boolean one,        boolean many,        String name    ) {
        this.one = one;
        this.many = many;
        this.name = name;
    }


    public boolean getOne() {
        return one;
    }

    public void setOne(boolean one) {
        this.one = one;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jsonldConverter_Type getJsonldconverter_type() {
        return jsonldconverter_type;
    }

    public void setJsonldconverter_type(jsonldConverter_Type jsonldconverter_type) {
        this.jsonldconverter_type = jsonldconverter_type;
    }
    public jsonldConverter_Entity getJsonldconverter_entity() {
        return jsonldconverter_entity;
    }

    public void setJsonldconverter_entity(jsonldConverter_Entity jsonldconverter_entity) {
        this.jsonldconverter_entity = jsonldconverter_entity;
    }

}