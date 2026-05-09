





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescriptor extends WorkBreakdownElement, Descriptor {






    private uma_Task uma_task;




    private List<uma_Section> uma_sections;


    public uma_TaskDescriptor(
    ) {
        super(
        );
        this.uma_sections = new ArrayList<>();
    }

    public uma_TaskDescriptor(
        ArrayList<uma_Section> uma_sections    ) {
        this.uma_sections = uma_sections;
    }


    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}