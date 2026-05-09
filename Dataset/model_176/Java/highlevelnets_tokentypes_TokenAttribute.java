





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_tokentypes_TokenAttribute extends IEntityIdentifiable {

    private String type;
    private String name;
    private String value;



    public highlevelnets_tokentypes_TokenAttribute(
        String type,        String name,        String value    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.value = value;
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


}