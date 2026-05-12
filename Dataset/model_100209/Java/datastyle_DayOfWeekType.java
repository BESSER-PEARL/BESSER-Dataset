





import java.util.List;
import java.util.ArrayList;

public class datastyle_DayOfWeekType  {

    private String calendar;
    private String style;





    private datastyle_DateStyleType datastyle_datestyletype;


    public datastyle_DayOfWeekType(
        String calendar,        String style    ) {
        this.calendar = calendar;
        this.style = style;
    }


    public String getCalendar() {
        return calendar;
    }

    public void setCalendar(String calendar) {
        this.calendar = calendar;
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