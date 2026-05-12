





import java.util.List;
import java.util.ArrayList;

public class XHTML_Object extends Attrs, Special, HeadMisc {

    private String declare;



    public XHTML_Object(
        String declare    ) {
        super(
        );
        this.declare = declare;
    }


    public String getDeclare() {
        return declare;
    }

    public void setDeclare(String declare) {
        this.declare = declare;
    }


}