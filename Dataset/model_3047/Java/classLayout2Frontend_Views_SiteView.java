





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Views_SiteView  {

    private String displayName;
    private String templateColor;
    private String name;
    private String templateName;



    public classLayout2Frontend_Views_SiteView(
        String displayName,        String templateColor,        String name,        String templateName    ) {
        this.displayName = displayName;
        this.templateColor = templateColor;
        this.name = name;
        this.templateName = templateName;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getTemplatecolor() {
        return templateColor;
    }

    public void setTemplatecolor(String templateColor) {
        this.templateColor = templateColor;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTemplatename() {
        return templateName;
    }

    public void setTemplatename(String templateName) {
        this.templateName = templateName;
    }


}