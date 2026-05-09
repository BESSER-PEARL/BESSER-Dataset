





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ExceptionEvent extends Event {

    private String ExceptionCauseStackTrace;
    private String ExceptionCauseTitle;
    private String ExceptionTitle;
    private String ExceptionStackTrace;



    public esmodel_events_ExceptionEvent(
        String ExceptionCauseStackTrace,        String ExceptionCauseTitle,        String ExceptionTitle,        String ExceptionStackTrace    ) {
        super(
        );
        this.ExceptionCauseStackTrace = ExceptionCauseStackTrace;
        this.ExceptionCauseTitle = ExceptionCauseTitle;
        this.ExceptionTitle = ExceptionTitle;
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
    public String getExceptionstacktrace() {
        return ExceptionStackTrace;
    }

    public void setExceptionstacktrace(String ExceptionStackTrace) {
        this.ExceptionStackTrace = ExceptionStackTrace;
    }


}