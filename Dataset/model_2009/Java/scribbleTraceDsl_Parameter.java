





import java.util.List;
import java.util.ArrayList;

public class scribbleTraceDsl_Parameter  {

    private String type;
    private String value;





    private scribbleTraceDsl_Messagetransfer scribbletracedsl_messagetransfer;


    public scribbleTraceDsl_Parameter(
        String type,        String value    ) {
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public scribbleTraceDsl_Messagetransfer getScribbletracedsl_messagetransfer() {
        return scribbletracedsl_messagetransfer;
    }

    public void setScribbletracedsl_messagetransfer(scribbleTraceDsl_Messagetransfer scribbletracedsl_messagetransfer) {
        this.scribbletracedsl_messagetransfer = scribbletracedsl_messagetransfer;
    }

}