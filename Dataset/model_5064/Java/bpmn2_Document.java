





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Document  {






    private bpmn2_DataOutput bpmn2_dataoutput;




    private bpmn2_Task bpmn2_task;




    private bpmn2_DataInput bpmn2_datainput;


    public bpmn2_Document(
    ) {
    }



    public bpmn2_DataOutput getBpmn2_dataoutput() {
        return bpmn2_dataoutput;
    }

    public void setBpmn2_dataoutput(bpmn2_DataOutput bpmn2_dataoutput) {
        this.bpmn2_dataoutput = bpmn2_dataoutput;
    }
    public bpmn2_Task getBpmn2_task() {
        return bpmn2_task;
    }

    public void setBpmn2_task(bpmn2_Task bpmn2_task) {
        this.bpmn2_task = bpmn2_task;
    }
    public bpmn2_DataInput getBpmn2_datainput() {
        return bpmn2_datainput;
    }

    public void setBpmn2_datainput(bpmn2_DataInput bpmn2_datainput) {
        this.bpmn2_datainput = bpmn2_datainput;
    }

}