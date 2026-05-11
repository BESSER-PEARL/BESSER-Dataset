





import java.util.List;
import java.util.ArrayList;

public class myDsl_BaseException  {

    private String errorCode;
    private String message;





    private myDsl_ExceptionMapper mydsl_exceptionmapper;


    public myDsl_BaseException(
        String errorCode,        String message    ) {
        this.errorCode = errorCode;
        this.message = message;
    }


    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public myDsl_ExceptionMapper getMydsl_exceptionmapper() {
        return mydsl_exceptionmapper;
    }

    public void setMydsl_exceptionmapper(myDsl_ExceptionMapper mydsl_exceptionmapper) {
        this.mydsl_exceptionmapper = mydsl_exceptionmapper;
    }

}