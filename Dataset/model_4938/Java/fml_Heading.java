





import java.util.List;
import java.util.ArrayList;

public class fml_Heading extends DisplayElement {

    private String Text;
    private String Level;



    public fml_Heading(
        String Text,        String Level    ) {
        super(
        );
        this.Text = Text;
        this.Level = Level;
    }


    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }
    public String getLevel() {
        return Level;
    }

    public void setLevel(String Level) {
        this.Level = Level;
    }


}