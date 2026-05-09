





import java.util.List;
import java.util.ArrayList;

public class vml_Slice  {

    private String title;
    private int value;



    public vml_Slice(
        String title,        int value    ) {
        this.title = title;
        this.value = value;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}