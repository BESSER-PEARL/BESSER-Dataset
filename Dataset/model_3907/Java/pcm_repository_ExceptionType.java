





import java.util.List;
import java.util.ArrayList;

public class pcm_repository_ExceptionType  {

    private String exceptionMessage;
    private String exceptionName;



    public pcm_repository_ExceptionType(
        String exceptionMessage,        String exceptionName    ) {
        this.exceptionMessage = exceptionMessage;
        this.exceptionName = exceptionName;
    }


    public String getExceptionmessage() {
        return exceptionMessage;
    }

    public void setExceptionmessage(String exceptionMessage) {
        this.exceptionMessage = exceptionMessage;
    }
    public String getExceptionname() {
        return exceptionName;
    }

    public void setExceptionname(String exceptionName) {
        this.exceptionName = exceptionName;
    }


}