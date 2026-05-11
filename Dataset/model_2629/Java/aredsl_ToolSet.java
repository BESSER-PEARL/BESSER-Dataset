





import java.util.List;
import java.util.ArrayList;

public class aredsl_ToolSet  {

    private String id;
    private String description;





    private aredsl_Editor aredsl_editor;


    public aredsl_ToolSet(
        String id,        String description    ) {
        this.id = id;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public aredsl_Editor getAredsl_editor() {
        return aredsl_editor;
    }

    public void setAredsl_editor(aredsl_Editor aredsl_editor) {
        this.aredsl_editor = aredsl_editor;
    }

}