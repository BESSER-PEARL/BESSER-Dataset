





import java.util.List;
import java.util.ArrayList;

public class documentation_ListItem  {

    private String text;





    private documentation_List documentation_list;


    public documentation_ListItem(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public documentation_List getDocumentation_list() {
        return documentation_list;
    }

    public void setDocumentation_list(documentation_List documentation_list) {
        this.documentation_list = documentation_list;
    }

}