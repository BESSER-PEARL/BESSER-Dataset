





import java.util.List;
import java.util.ArrayList;

public class uppaal_NTA extends core_NamedElement, core_CommentableElement {






    private GlobalDeclarations globaldeclarations;




    private SystemDeclarations systemdeclarations;




    private List<Template> templates;


    public uppaal_NTA(
    ) {
        super(
        );
        this.templates = new ArrayList<>();
    }

    public uppaal_NTA(
        ArrayList<Template> templates    ) {
        this.templates = templates;
    }


    public GlobalDeclarations getGlobaldeclarations() {
        return globaldeclarations;
    }

    public void setGlobaldeclarations(GlobalDeclarations globaldeclarations) {
        this.globaldeclarations = globaldeclarations;
    }
    public SystemDeclarations getSystemdeclarations() {
        return systemdeclarations;
    }

    public void setSystemdeclarations(SystemDeclarations systemdeclarations) {
        this.systemdeclarations = systemdeclarations;
    }
    public List<Template> getTemplates() {
        return templates;
    }

    public void addTemplate(Template template) {
        this.templates.add(template);
    }

}