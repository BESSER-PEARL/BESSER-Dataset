





import java.util.List;
import java.util.ArrayList;

public class datastyle_DayType  {

    private String style;
    private String calendar;





    private datastyle_DateStyleType datastyle_datestyletype;


    public datastyle_DayType(
        String style,        String calendar    ) {
        this.style = style;
        this.calendar = calendar;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getCalendar() {
        return calendar;
    }

    public void setCalendar(String calendar) {
        this.calendar = calendar;
    }

    public datastyle_DateStyleType getDatastyle_datestyletype() {
        return datastyle_datestyletype;
    }

    public void setDatastyle_datestyletype(datastyle_DateStyleType datastyle_datestyletype) {
        this.datastyle_datestyletype = datastyle_datestyletype;
    }

}