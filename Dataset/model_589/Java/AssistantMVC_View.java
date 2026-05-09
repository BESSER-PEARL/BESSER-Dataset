





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String name;
    private String color;





    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_View(
        String name,        String color    ) {
        super(
        );
        this.name = name;
        this.color = color;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}