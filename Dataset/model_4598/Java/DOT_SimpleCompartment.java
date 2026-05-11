





import java.util.List;
import java.util.ArrayList;

public class DOT_SimpleCompartment extends Compartment {

    private String content;



    public DOT_SimpleCompartment(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}