





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ExceptionEvent extends Event {

    private String ExceptionStackTrace;
    private String ExceptionTitle;
    private String ExceptionCauseTitle;
    private String ExceptionCauseStackTrace;



    public esmodel_events_ExceptionEvent(
        String ExceptionStackTrace,        String ExceptionTitle,        String ExceptionCauseTitle,        String ExceptionCauseStackTrace    ) {
        super(
        );
        this.ExceptionStackTrace = ExceptionStackTrace;
        this.ExceptionTitle = ExceptionTitle;
        this.ExceptionCauseTitle = ExceptionCauseTitle;
        this.ExceptionCauseStackTrace = ExceptionCauseStackTrace;
    }


    public String getExceptionstacktrace() {
        return ExceptionStackTrace;
    }

    public void setExceptionstacktrace(String ExceptionStackTrace) {
        this.ExceptionStackTrace = ExceptionStackTrace;
    }
    public String getExceptiontitle() {
        return ExceptionTitle;
    }

    public void setExceptiontitle(String ExceptionTitle) {
        this.ExceptionTitle = ExceptionTitle;
    }
    public String getExceptioncausetitle() {
        return ExceptionCauseTitle;
    }

    public void setExceptioncausetitle(String ExceptionCauseTitle) {
        this.ExceptionCauseTitle = ExceptionCauseTitle;
    }
    public String getExceptioncausestacktrace() {
        return ExceptionCauseStackTrace;
    }

    public void setExceptioncausestacktrace(String ExceptionCauseStackTrace) {
        this.ExceptionCauseStackTrace = ExceptionCauseStackTrace;
    }


}