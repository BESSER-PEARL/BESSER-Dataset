





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Style  {

    private int age;
    private String type;





    private AssistantMVC_View assistantmvc_view;


    public AssistantMVC_Style(
        int age,        String type    ) {
        this.age = age;
        this.type = type;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public AssistantMVC_View getAssistantmvc_view() {
        return assistantmvc_view;
    }

    public void setAssistantmvc_view(AssistantMVC_View assistantmvc_view) {
        this.assistantmvc_view = assistantmvc_view;
    }

}