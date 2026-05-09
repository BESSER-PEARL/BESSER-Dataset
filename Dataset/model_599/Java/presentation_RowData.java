





import java.util.List;
import java.util.ArrayList;

public class presentation_RowData  {

    private String width;
    private String mixed;
    private String height;
    private String exclude;



    public presentation_RowData(
        String width,        String mixed,        String height,        String exclude    ) {
        this.width = width;
        this.mixed = mixed;
        this.height = height;
        this.exclude = exclude;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getExclude() {
        return exclude;
    }

    public void setExclude(String exclude) {
        this.exclude = exclude;
    }


}