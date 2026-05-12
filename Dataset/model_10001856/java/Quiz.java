





import java.util.List;
import java.util.ArrayList;

public class Quiz  {

    private String questions__;
    private String title;
    private String moduleName;



    public Quiz(
        String questions__,        String title,        String moduleName    ) {
        this.questions__ = questions__;
        this.title = title;
        this.moduleName = moduleName;
    }


    public String getQuestions__() {
        return questions__;
    }

    public void setQuestions__(String questions__) {
        this.questions__ = questions__;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }


}