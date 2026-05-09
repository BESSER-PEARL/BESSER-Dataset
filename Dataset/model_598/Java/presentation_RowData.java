





import java.util.List;
import java.util.ArrayList;

public class presentation_RowData  {

    private String exclude;
    private String height;
    private String mixed;
    private String width;



    public presentation_RowData(
        String exclude,        String height,        String mixed,        String width    ) {
        this.exclude = exclude;
        this.height = height;
        this.mixed = mixed;
        this.width = width;
    }


    public String getExclude() {
        return exclude;
    }

    public void setExclude(String exclude) {
        this.exclude = exclude;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}