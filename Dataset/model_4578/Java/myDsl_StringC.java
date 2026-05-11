





import java.util.List;
import java.util.ArrayList;

public class myDsl_StringC extends primary_expression {

    private String string;



    public myDsl_StringC(
        String string    ) {
        super(
        );
        this.string = string;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }


}