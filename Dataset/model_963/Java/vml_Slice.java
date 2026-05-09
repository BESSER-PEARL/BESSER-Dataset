





import java.util.List;
import java.util.ArrayList;

public class vml_Slice extends DiagramElement {

    private int value;
    private String title;





    private vml_Pie vml_pie;


    public vml_Slice(
        int value,        String title    ) {
        super(
        );
        this.value = value;
        this.title = title;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public vml_Pie getVml_pie() {
        return vml_pie;
    }

    public void setVml_pie(vml_Pie vml_pie) {
        this.vml_pie = vml_pie;
    }

}