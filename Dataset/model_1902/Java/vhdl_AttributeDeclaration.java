





import java.util.List;
import java.util.ArrayList;

public class vhdl_AttributeDeclaration extends BlockDeclarativeItem {

    private String type_id;
    private String name;
    private String type_keyword;



    public vhdl_AttributeDeclaration(
        String type_id,        String name,        String type_keyword    ) {
        super(
        );
        this.type_id = type_id;
        this.name = name;
        this.type_keyword = type_keyword;
    }


    public String getType_id() {
        return type_id;
    }

    public void setType_id(String type_id) {
        this.type_id = type_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType_keyword() {
        return type_keyword;
    }

    public void setType_keyword(String type_keyword) {
        this.type_keyword = type_keyword;
    }


}