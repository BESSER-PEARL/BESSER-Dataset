





import java.util.List;
import java.util.ArrayList;

public class bootstrap_Section  {

    private String description;
    private String title;





    private bootstrap_Page bootstrap_page;




    private List<bootstrap_Widget> bootstrap_widgets;




    private bootstrap_Page bootstrap_page;




    private bootstrap_Widget bootstrap_widget;


    public bootstrap_Section(
        String description,        String title    ) {
        this.description = description;
        this.title = title;
        this.bootstrap_widgets = new ArrayList<>();
    }

    public bootstrap_Section(
        String description,        String title        ArrayList<bootstrap_Widget> bootstrap_widgets    ) {
        this.description = description;
        this.title = title;
        this.bootstrap_widgets = bootstrap_widgets;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public bootstrap_Page getBootstrap_page() {
        return bootstrap_page;
    }

    public void setBootstrap_page(bootstrap_Page bootstrap_page) {
        this.bootstrap_page = bootstrap_page;
    }
    public List<bootstrap_Widget> getBootstrap_widgets() {
        return bootstrap_widgets;
    }

    public void addBootstrap_widget(Bootstrap_widget bootstrap_widget) {
        this.bootstrap_widgets.add(bootstrap_widget);
    }
    public bootstrap_Page getBootstrap_page() {
        return bootstrap_page;
    }

    public void setBootstrap_page(bootstrap_Page bootstrap_page) {
        this.bootstrap_page = bootstrap_page;
    }
    public bootstrap_Widget getBootstrap_widget() {
        return bootstrap_widget;
    }

    public void setBootstrap_widget(bootstrap_Widget bootstrap_widget) {
        this.bootstrap_widget = bootstrap_widget;
    }

}