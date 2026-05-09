





import java.util.List;
import java.util.ArrayList;

public class SimplePDL_Guidance  {

    private String text;





    private SimplePDL_ProcessElement simplepdl_processelement;




    private SimplePDL_Process simplepdl_process;


    public SimplePDL_Guidance(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public SimplePDL_ProcessElement getSimplepdl_processelement() {
        return simplepdl_processelement;
    }

    public void setSimplepdl_processelement(SimplePDL_ProcessElement simplepdl_processelement) {
        this.simplepdl_processelement = simplepdl_processelement;
    }
    public SimplePDL_Process getSimplepdl_process() {
        return simplepdl_process;
    }

    public void setSimplepdl_process(SimplePDL_Process simplepdl_process) {
        this.simplepdl_process = simplepdl_process;
    }

}