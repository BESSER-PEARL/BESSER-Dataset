





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String fontName;





    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_View(
        String fontName    ) {
        super(
        );
        this.fontName = fontName;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}