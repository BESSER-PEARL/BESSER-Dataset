





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Project  {

    private String name;





    private List<classLayout2Frontend_ContainerView> classlayout2frontend_containerviews;




    private List<classLayout2Frontend_PageView> classlayout2frontend_pageviews;


    public classLayout2Frontend_Project(
        String name    ) {
        this.name = name;
        this.classlayout2frontend_containerviews = new ArrayList<>();
        this.classlayout2frontend_pageviews = new ArrayList<>();
    }

    public classLayout2Frontend_Project(
        String name        ArrayList<classLayout2Frontend_ContainerView> classlayout2frontend_containerviews,        ArrayList<classLayout2Frontend_PageView> classlayout2frontend_pageviews    ) {
        this.name = name;
        this.classlayout2frontend_containerviews = classlayout2frontend_containerviews;
        this.classlayout2frontend_pageviews = classlayout2frontend_pageviews;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classLayout2Frontend_ContainerView> getClasslayout2frontend_containerviews() {
        return classlayout2frontend_containerviews;
    }

    public void addClasslayout2frontend_containerview(Classlayout2frontend_containerview classlayout2frontend_containerview) {
        this.classlayout2frontend_containerviews.add(classlayout2frontend_containerview);
    }
    public List<classLayout2Frontend_PageView> getClasslayout2frontend_pageviews() {
        return classlayout2frontend_pageviews;
    }

    public void addClasslayout2frontend_pageview(Classlayout2frontend_pageview classlayout2frontend_pageview) {
        this.classlayout2frontend_pageviews.add(classlayout2frontend_pageview);
    }

}