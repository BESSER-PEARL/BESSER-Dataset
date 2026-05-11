





import java.util.List;
import java.util.ArrayList;

public class html5_container  {

    private String class_;





    private List<html5_container> html5_containers;




    private html5_html html5_html;


    public html5_container(
        String class_    ) {
        this.class_ = class_;
        this.html5_containers = new ArrayList<>();
    }

    public html5_container(
        String class_        ArrayList<html5_container> html5_containers    ) {
        this.class_ = class_;
        this.html5_containers = html5_containers;
    }

    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }

    public List<html5_container> getHtml5_containers() {
        return html5_containers;
    }

    public void addHtml5_container(Html5_container html5_container) {
        this.html5_containers.add(html5_container);
    }
    public html5_html getHtml5_html() {
        return html5_html;
    }

    public void setHtml5_html(html5_html html5_html) {
        this.html5_html = html5_html;
    }

}