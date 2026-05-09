





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Guidance extends ProcessElement {

    private String text;





    private simplepdl_ProcessElement simplepdl_processelement;


    public simplepdl_Guidance(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public simplepdl_ProcessElement getSimplepdl_processelement() {
        return simplepdl_processelement;
    }

    public void setSimplepdl_processelement(simplepdl_ProcessElement simplepdl_processelement) {
        this.simplepdl_processelement = simplepdl_processelement;
    }

}