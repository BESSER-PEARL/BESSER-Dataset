





import java.util.List;
import java.util.ArrayList;

public class typedef_Exception extends Type {

    private String exceptionType;



    public typedef_Exception(
        String exceptionType    ) {
        super(
        );
        this.exceptionType = exceptionType;
    }


    public String getExceptiontype() {
        return exceptionType;
    }

    public void setExceptiontype(String exceptionType) {
        this.exceptionType = exceptionType;
    }


}