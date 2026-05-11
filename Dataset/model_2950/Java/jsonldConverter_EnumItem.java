





import java.util.List;
import java.util.ArrayList;

public class jsonldConverter_EnumItem  {

    private String type;
    private String name;





    private jsonldConverter_Enum jsonldconverter_enum;


    public jsonldConverter_EnumItem(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
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

    public jsonldConverter_Enum getJsonldconverter_enum() {
        return jsonldconverter_enum;
    }

    public void setJsonldconverter_enum(jsonldConverter_Enum jsonldconverter_enum) {
        this.jsonldconverter_enum = jsonldconverter_enum;
    }

}