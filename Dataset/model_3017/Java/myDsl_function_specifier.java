





import java.util.List;
import java.util.ArrayList;

public class myDsl_function_specifier  {

    private String noreturn;
    private String inline;



    public myDsl_function_specifier(
        String noreturn,        String inline    ) {
        this.noreturn = noreturn;
        this.inline = inline;
    }


    public String getNoreturn() {
        return noreturn;
    }

    public void setNoreturn(String noreturn) {
        this.noreturn = noreturn;
    }
    public String getInline() {
        return inline;
    }

    public void setInline(String inline) {
        this.inline = inline;
    }


}