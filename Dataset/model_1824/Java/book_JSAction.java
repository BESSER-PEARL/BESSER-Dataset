





import java.util.List;
import java.util.ArrayList;

public class book_JSAction extends Action {

    private String javaScript;



    public book_JSAction(
        String javaScript    ) {
        super(
        );
        this.javaScript = javaScript;
    }


    public String getJavascript() {
        return javaScript;
    }

    public void setJavascript(String javaScript) {
        this.javaScript = javaScript;
    }


}