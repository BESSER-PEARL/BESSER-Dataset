





import java.util.List;
import java.util.ArrayList;

public class frameweb_TagLib extends Package {

    private String prefix;





    private frameweb_Template frameweb_template;




    private frameweb_Page frameweb_page;


    public frameweb_TagLib(
        String prefix    ) {
        super(
        );
        this.prefix = prefix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public frameweb_Template getFrameweb_template() {
        return frameweb_template;
    }

    public void setFrameweb_template(frameweb_Template frameweb_template) {
        this.frameweb_template = frameweb_template;
    }
    public frameweb_Page getFrameweb_page() {
        return frameweb_page;
    }

    public void setFrameweb_page(frameweb_Page frameweb_page) {
        this.frameweb_page = frameweb_page;
    }

}