





import java.util.List;
import java.util.ArrayList;

public class expressions_ast_Expression  {

    private String text;
    private String type;



    public expressions_ast_Expression(
        String text,        String type    ) {
        this.text = text;
        this.type = type;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}