





import java.util.List;
import java.util.ArrayList;

public class ErrorCodeException  {

    private String throwable;
    private String errorCodeMessage;
    private None errorCode;



    public ErrorCodeException(
        String throwable,        String errorCodeMessage,        None errorCode    ) {
        this.throwable = throwable;
        this.errorCodeMessage = errorCodeMessage;
        this.errorCode = errorCode;
    }


    public String getThrowable() {
        return throwable;
    }

    public void setThrowable(String throwable) {
        this.throwable = throwable;
    }
    public String getErrorcodemessage() {
        return errorCodeMessage;
    }

    public void setErrorcodemessage(String errorCodeMessage) {
        this.errorCodeMessage = errorCodeMessage;
    }
    public None getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(None errorCode) {
        this.errorCode = errorCode;
    }


}