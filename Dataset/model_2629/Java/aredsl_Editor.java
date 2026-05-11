





import java.util.List;
import java.util.ArrayList;

public class aredsl_Editor  {

    private String name;
    private String queryLanguageKind;
    private String description;
    private String fileExtension;



    public aredsl_Editor(
        String name,        String queryLanguageKind,        String description,        String fileExtension    ) {
        this.name = name;
        this.queryLanguageKind = queryLanguageKind;
        this.description = description;
        this.fileExtension = fileExtension;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQuerylanguagekind() {
        return queryLanguageKind;
    }

    public void setQuerylanguagekind(String queryLanguageKind) {
        this.queryLanguageKind = queryLanguageKind;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
    }


}