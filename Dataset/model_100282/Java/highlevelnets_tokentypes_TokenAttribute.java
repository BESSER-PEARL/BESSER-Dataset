





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_tokentypes_TokenAttribute extends IEntityIdentifiable {

    private String value;
    private String type;
    private String name;



    public highlevelnets_tokentypes_TokenAttribute(
        String value,        String type,        String name    ) {
        super(
        );
        this.value = value;
        this.type = type;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
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


}