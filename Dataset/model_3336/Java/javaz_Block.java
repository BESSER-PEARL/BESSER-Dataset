





import java.util.List;
import java.util.ArrayList;

public class javaz_Block  {

    private String content;





    private javaz_Method javaz_method;


    public javaz_Block(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public javaz_Method getJavaz_method() {
        return javaz_method;
    }

    public void setJavaz_method(javaz_Method javaz_method) {
        this.javaz_method = javaz_method;
    }

}