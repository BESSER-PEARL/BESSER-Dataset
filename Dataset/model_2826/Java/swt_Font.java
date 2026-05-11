





import java.util.List;
import java.util.ArrayList;

public class swt_Font  {

    private int height;
    private String name;
    private int style;



    public swt_Font(
        int height,        String name,        int style    ) {
        this.height = height;
        this.name = name;
        this.style = style;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStyle() {
        return style;
    }

    public void setStyle(int style) {
        this.style = style;
    }


}