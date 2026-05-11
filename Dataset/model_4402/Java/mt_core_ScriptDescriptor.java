





import java.util.List;
import java.util.ArrayList;

public class mt_core_ScriptDescriptor extends ASTNode {

    private String type;
    private String name;
    private String description;



    public mt_core_ScriptDescriptor(
        String type,        String name,        String description    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.description = description;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}