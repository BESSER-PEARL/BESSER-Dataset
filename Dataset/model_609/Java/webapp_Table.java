





import java.util.List;
import java.util.ArrayList;

public class webapp_Table  {

    private String name;
    private String charset;





    private webapp_Model webapp_model;


    public webapp_Table(
        String name,        String charset    ) {
        this.name = name;
        this.charset = charset;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCharset() {
        return charset;
    }

    public void setCharset(String charset) {
        this.charset = charset;
    }

    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }

}