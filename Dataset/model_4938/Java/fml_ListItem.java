





import java.util.List;
import java.util.ArrayList;

public class fml_ListItem  {

    private String Text;





    private fml_List fml_list;


    public fml_ListItem(
        String Text    ) {
        this.Text = Text;
    }


    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }

    public fml_List getFml_list() {
        return fml_list;
    }

    public void setFml_list(fml_List fml_list) {
        this.fml_list = fml_list;
    }

}