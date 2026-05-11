





import java.util.List;
import java.util.ArrayList;

public class cm_repository_ExceptionType  {

    private String name;
    private String message;



    public cm_repository_ExceptionType(
        String name,        String message    ) {
        this.name = name;
        this.message = message;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}