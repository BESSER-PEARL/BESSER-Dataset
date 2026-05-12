





import java.util.List;
import java.util.ArrayList;

public class PNML_AnyElement  {

    private String text;
    private String name;



    public PNML_AnyElement(
        String text,        String name    ) {
        this.text = text;
        this.name = name;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}