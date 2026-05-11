





import java.util.List;
import java.util.ArrayList;

public class viewpoint_audit_TemplateInformationSection extends InformationSection {

    private String templatePath;



    public viewpoint_audit_TemplateInformationSection(
        String templatePath    ) {
        super(
        );
        this.templatePath = templatePath;
    }


    public String getTemplatepath() {
        return templatePath;
    }

    public void setTemplatepath(String templatePath) {
        this.templatePath = templatePath;
    }


}