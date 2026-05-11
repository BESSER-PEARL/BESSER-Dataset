





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppComment extends CppModelElement {

    private boolean singleLine;
    private String content;
    private boolean multiLine;



    public Metamodelo_Cpp_CppComment(
        boolean singleLine,        String content,        boolean multiLine    ) {
        super(
        );
        this.singleLine = singleLine;
        this.content = content;
        this.multiLine = multiLine;
    }


    public boolean getSingleline() {
        return singleLine;
    }

    public void setSingleline(boolean singleLine) {
        this.singleLine = singleLine;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public boolean getMultiline() {
        return multiLine;
    }

    public void setMultiline(boolean multiLine) {
        this.multiLine = multiLine;
    }


}