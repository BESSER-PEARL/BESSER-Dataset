





import java.util.List;
import java.util.ArrayList;

public class TokenTrace_TokenTrace  {

    private String tokenTraceType;
    private String name;
    private String message;



    public TokenTrace_TokenTrace(
        String tokenTraceType,        String name,        String message    ) {
        this.tokenTraceType = tokenTraceType;
        this.name = name;
        this.message = message;
    }


    public String getTokentracetype() {
        return tokenTraceType;
    }

    public void setTokentracetype(String tokenTraceType) {
        this.tokenTraceType = tokenTraceType;
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