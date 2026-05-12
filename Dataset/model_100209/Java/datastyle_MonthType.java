





import java.util.List;
import java.util.ArrayList;

public class datastyle_MonthType  {

    private String textual;
    private String calendar;
    private String possessiveForm;
    private String style;





    private datastyle_DateStyleType datastyle_datestyletype;


    public datastyle_MonthType(
        String textual,        String calendar,        String possessiveForm,        String style    ) {
        this.textual = textual;
        this.calendar = calendar;
        this.possessiveForm = possessiveForm;
        this.style = style;
    }


    public String getTextual() {
        return textual;
    }

    public void setTextual(String textual) {
        this.textual = textual;
    }
    public String getCalendar() {
        return calendar;
    }

    public void setCalendar(String calendar) {
        this.calendar = calendar;
    }
    public String getPossessiveform() {
        return possessiveForm;
    }

    public void setPossessiveform(String possessiveForm) {
        this.possessiveForm = possessiveForm;
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