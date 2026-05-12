





import java.util.List;
import java.util.ArrayList;

public class sqls_EnumElement  {

    private String name;
    private String text;



    public sqls_EnumElement(
        String name,        String text    ) {
        this.name = name;
        this.text = text;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}