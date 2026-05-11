





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_ElementView  {

    private String description;
    private String name;
    private String displayName;





    private classLayout2Frontend_PageView classlayout2frontend_pageview;




    private classLayout2Frontend_ContainerView classlayout2frontend_containerview;


    public classLayout2Frontend_ElementView(
        String description,        String name,        String displayName    ) {
        this.description = description;
        this.name = name;
        this.displayName = displayName;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }

    public classLayout2Frontend_PageView getClasslayout2frontend_pageview() {
        return classlayout2frontend_pageview;
    }

    public void setClasslayout2frontend_pageview(classLayout2Frontend_PageView classlayout2frontend_pageview) {
        this.classlayout2frontend_pageview = classlayout2frontend_pageview;
    }
    public classLayout2Frontend_ContainerView getClasslayout2frontend_containerview() {
        return classlayout2frontend_containerview;
    }

    public void setClasslayout2frontend_containerview(classLayout2Frontend_ContainerView classlayout2frontend_containerview) {
        this.classlayout2frontend_containerview = classlayout2frontend_containerview;
    }

}