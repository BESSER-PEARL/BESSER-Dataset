





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_tokentypes_TokenAttribute extends IEntityIdentifiable {

    private String value;
    private String name;
    private String type;



    public highlevelnets_tokentypes_TokenAttribute(
        String value,        String name,        String type    ) {
        super(
        );
        this.value = value;
        this.name = name;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}