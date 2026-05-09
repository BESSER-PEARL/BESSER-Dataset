





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ExceptionEvent extends Event {

    private String ExceptionStackTrace;
    private String ExceptionCauseStackTrace;
    private String ExceptionCauseTitle;
    private String ExceptionTitle;



    public esmodel_events_ExceptionEvent(
        String ExceptionStackTrace,        String ExceptionCauseStackTrace,        String ExceptionCauseTitle,        String ExceptionTitle    ) {
        super(
        );
        this.ExceptionStackTrace = ExceptionStackTrace;
        this.ExceptionCauseStackTrace = ExceptionCauseStackTrace;
        this.ExceptionCauseTitle = ExceptionCauseTitle;
        this.ExceptionTitle = ExceptionTitle;
    }


    public String getExceptionstacktrace() {
        return ExceptionStackTrace;
    }

    public void setExceptionstacktrace(String ExceptionStackTrace) {
        this.ExceptionStackTrace = ExceptionStackTrace;
    }
    public String getExceptioncausestacktrace() {
        return ExceptionCauseStackTrace;
    }

    public void setExceptioncausestacktrace(String ExceptionCauseStackTrace) {
        this.ExceptionCauseStackTrace = ExceptionCauseStackTrace;
    }
    public String getExceptioncausetitle() {
        return ExceptionCauseTitle;
    }

    public void setExceptioncausetitle(String ExceptionCauseTitle) {
        this.ExceptionCauseTitle = ExceptionCauseTitle;
    }
    public String getExceptiontitle() {
        return ExceptionTitle;
    }

    public void setExceptiontitle(String ExceptionTitle) {
        this.ExceptionTitle = ExceptionTitle;
    }


}