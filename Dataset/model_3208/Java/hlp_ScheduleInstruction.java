





import java.util.List;
import java.util.ArrayList;

public class hlp_ScheduleInstruction  {






    private hlp_HighLevelProgram hlp_highlevelprogram;




    private List<hlp_Task> hlp_tasks;


    public hlp_ScheduleInstruction(
    ) {
        this.hlp_tasks = new ArrayList<>();
    }

    public hlp_ScheduleInstruction(
        ArrayList<hlp_Task> hlp_tasks    ) {
        this.hlp_tasks = hlp_tasks;
    }


    public hlp_HighLevelProgram getHlp_highlevelprogram() {
        return hlp_highlevelprogram;
    }

    public void setHlp_highlevelprogram(hlp_HighLevelProgram hlp_highlevelprogram) {
        this.hlp_highlevelprogram = hlp_highlevelprogram;
    }
    public List<hlp_Task> getHlp_tasks() {
        return hlp_tasks;
    }

    public void addHlp_task(Hlp_task hlp_task) {
        this.hlp_tasks.add(hlp_task);
    }

}