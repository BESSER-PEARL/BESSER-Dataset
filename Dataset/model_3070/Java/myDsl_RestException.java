





import java.util.List;
import java.util.ArrayList;

public class myDsl_RestException  {

    private String message;
    private String statusCode;





    private myDsl_RestExceptionList mydsl_restexceptionlist;




    private myDsl_ExceptionMapper mydsl_exceptionmapper;


    public myDsl_RestException(
        String message,        String statusCode    ) {
        this.message = message;
        this.statusCode = statusCode;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getStatuscode() {
        return statusCode;
    }

    public void setStatuscode(String statusCode) {
        this.statusCode = statusCode;
    }

    public myDsl_RestExceptionList getMydsl_restexceptionlist() {
        return mydsl_restexceptionlist;
    }

    public void setMydsl_restexceptionlist(myDsl_RestExceptionList mydsl_restexceptionlist) {
        this.mydsl_restexceptionlist = mydsl_restexceptionlist;
    }
    public myDsl_ExceptionMapper getMydsl_exceptionmapper() {
        return mydsl_exceptionmapper;
    }

    public void setMydsl_exceptionmapper(myDsl_ExceptionMapper mydsl_exceptionmapper) {
        this.mydsl_exceptionmapper = mydsl_exceptionmapper;
    }

}