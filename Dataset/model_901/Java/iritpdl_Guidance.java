





import java.util.List;
import java.util.ArrayList;

public class iritpdl_Guidance  {

    private String text;





    private iritpdl_Process iritpdl_process;




    private iritpdl_ProcessElement iritpdl_processelement;


    public iritpdl_Guidance(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public iritpdl_Process getIritpdl_process() {
        return iritpdl_process;
    }

    public void setIritpdl_process(iritpdl_Process iritpdl_process) {
        this.iritpdl_process = iritpdl_process;
    }
    public iritpdl_ProcessElement getIritpdl_processelement() {
        return iritpdl_processelement;
    }

    public void setIritpdl_processelement(iritpdl_ProcessElement iritpdl_processelement) {
        this.iritpdl_processelement = iritpdl_processelement;
    }

}