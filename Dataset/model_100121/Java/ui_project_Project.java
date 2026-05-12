





import java.util.List;
import java.util.ArrayList;

public class ui_project_Project extends schema_DataModelerNamedElement, schema_FunctionalElement {

    private String description;
    private String application;



    public ui_project_Project(
        String description,        String application    ) {
        super(
        );
        this.description = description;
        this.application = application;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getApplication() {
        return application;
    }

    public void setApplication(String application) {
        this.application = application;
    }


}