





import java.util.List;
import java.util.ArrayList;

public class webapp_Mapping  {

    private String right;
    private String left;





    private webapp_Properties webapp_properties;


    public webapp_Mapping(
        String right,        String left    ) {
        this.right = right;
        this.left = left;
    }


    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }
    public String getLeft() {
        return left;
    }

    public void setLeft(String left) {
        this.left = left;
    }

    public webapp_Properties getWebapp_properties() {
        return webapp_properties;
    }

    public void setWebapp_properties(webapp_Properties webapp_properties) {
        this.webapp_properties = webapp_properties;
    }

}