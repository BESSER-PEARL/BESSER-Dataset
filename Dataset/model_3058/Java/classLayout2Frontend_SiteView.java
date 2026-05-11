





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_SiteView  {

    private String displayName;
    private String templateColor;
    private String name;
    private String templateName;





    private List<classLayout2Frontend_PageView> classlayout2frontend_pageviews;




    private classLayout2Frontend_Project classlayout2frontend_project;


    public classLayout2Frontend_SiteView(
        String displayName,        String templateColor,        String name,        String templateName    ) {
        this.displayName = displayName;
        this.templateColor = templateColor;
        this.name = name;
        this.templateName = templateName;
        this.classlayout2frontend_pageviews = new ArrayList<>();
    }

    public classLayout2Frontend_SiteView(
        String displayName,        String templateColor,        String name,        String templateName        ArrayList<classLayout2Frontend_PageView> classlayout2frontend_pageviews    ) {
        this.displayName = displayName;
        this.templateColor = templateColor;
        this.name = name;
        this.templateName = templateName;
        this.classlayout2frontend_pageviews = classlayout2frontend_pageviews;
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

    public List<classLayout2Frontend_PageView> getClasslayout2frontend_pageviews() {
        return classlayout2frontend_pageviews;
    }

    public void addClasslayout2frontend_pageview(Classlayout2frontend_pageview classlayout2frontend_pageview) {
        this.classlayout2frontend_pageviews.add(classlayout2frontend_pageview);
    }
    public classLayout2Frontend_Project getClasslayout2frontend_project() {
        return classlayout2frontend_project;
    }

    public void setClasslayout2frontend_project(classLayout2Frontend_Project classlayout2frontend_project) {
        this.classlayout2frontend_project = classlayout2frontend_project;
    }

}