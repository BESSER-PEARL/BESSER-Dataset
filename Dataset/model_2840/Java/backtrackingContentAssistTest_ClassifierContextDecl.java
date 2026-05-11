





import java.util.List;
import java.util.ArrayList;

public class backtrackingContentAssistTest_ClassifierContextDecl extends ContextDecl {

    private String selfName;



    public backtrackingContentAssistTest_ClassifierContextDecl(
        String selfName    ) {
        super(
        );
        this.selfName = selfName;
    }


    public String getSelfname() {
        return selfName;
    }

    public void setSelfname(String selfName) {
        this.selfName = selfName;
    }


}