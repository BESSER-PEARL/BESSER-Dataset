





import java.util.List;
import java.util.ArrayList;

public class DATABASE_SYSTEM  {

    private boolean Content;





    private WELCOME_PAGE welcome_page;


    public DATABASE_SYSTEM(
        boolean Content    ) {
        this.Content = Content;
    }


    public boolean getContent() {
        return Content;
    }

    public void setContent(boolean Content) {
        this.Content = Content;
    }

    public WELCOME_PAGE getWelcome_page() {
        return welcome_page;
    }

    public void setWelcome_page(WELCOME_PAGE welcome_page) {
        this.welcome_page = welcome_page;
    }

}