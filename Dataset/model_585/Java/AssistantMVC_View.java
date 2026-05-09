





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_View extends Observer {

    private String fontName;
    private String fontColor;





    private AssistantMVC_Exam assistantmvc_exam;




    private AssistantMVC_Controller assistantmvc_controller;


    public AssistantMVC_View(
        String fontName,        String fontColor    ) {
        super(
        );
        this.fontName = fontName;
        this.fontColor = fontColor;
    }


    public String getFontname() {
        return fontName;
    }

    public void setFontname(String fontName) {
        this.fontName = fontName;
    }
    public String getFontcolor() {
        return fontColor;
    }

    public void setFontcolor(String fontColor) {
        this.fontColor = fontColor;
    }

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }
    public AssistantMVC_Controller getAssistantmvc_controller() {
        return assistantmvc_controller;
    }

    public void setAssistantmvc_controller(AssistantMVC_Controller assistantmvc_controller) {
        this.assistantmvc_controller = assistantmvc_controller;
    }

}