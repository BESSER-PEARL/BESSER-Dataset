





import java.util.List;
import java.util.ArrayList;

public class datastyle_MinutesType  {

    private String style;





    private datastyle_DateStyleType datastyle_datestyletype;


    public datastyle_MinutesType(
        String style    ) {
        this.style = style;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public datastyle_DateStyleType getDatastyle_datestyletype() {
        return datastyle_datestyletype;
    }

    public void setDatastyle_datestyletype(datastyle_DateStyleType datastyle_datestyletype) {
        this.datastyle_datestyletype = datastyle_datestyletype;
    }

}