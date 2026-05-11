





import java.util.List;
import java.util.ArrayList;

public class webapp_Page  {

    private String title;
    private boolean default;
    private String name;



    public webapp_Page(
        String title,        boolean default,        String name    ) {
        this.title = title;
        this.default = default;
        this.name = name;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}