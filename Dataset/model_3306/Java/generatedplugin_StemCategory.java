





import java.util.List;
import java.util.ArrayList;

public class generatedplugin_StemCategory  {

    private String name;
    private String parentId;
    private String id;





    private generatedplugin_Extension generatedplugin_extension;


    public generatedplugin_StemCategory(
        String name,        String parentId,        String id    ) {
        this.name = name;
        this.parentId = parentId;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParentid() {
        return parentId;
    }

    public void setParentid(String parentId) {
        this.parentId = parentId;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public generatedplugin_Extension getGeneratedplugin_extension() {
        return generatedplugin_extension;
    }

    public void setGeneratedplugin_extension(generatedplugin_Extension generatedplugin_extension) {
        this.generatedplugin_extension = generatedplugin_extension;
    }

}