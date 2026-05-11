





import java.util.List;
import java.util.ArrayList;

public class fml_Page  {

    private String Title;
    private boolean isWelcome;





    private fml_Page fml_page;




    private fml_Form fml_form;


    public fml_Page(
        String Title,        boolean isWelcome    ) {
        this.Title = Title;
        this.isWelcome = isWelcome;
    }


    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public boolean getIswelcome() {
        return isWelcome;
    }

    public void setIswelcome(boolean isWelcome) {
        this.isWelcome = isWelcome;
    }

    public fml_Page getFml_page() {
        return fml_page;
    }

    public void setFml_page(fml_Page fml_page) {
        this.fml_page = fml_page;
    }
    public fml_Form getFml_form() {
        return fml_form;
    }

    public void setFml_form(fml_Form fml_form) {
        this.fml_form = fml_form;
    }

}