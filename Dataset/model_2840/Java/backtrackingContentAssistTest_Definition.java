





import java.util.List;
import java.util.ArrayList;

public class backtrackingContentAssistTest_Definition  {

    private boolean static;
    private String constrainedName;
    private String constraintName;





    private backtrackingContentAssistTest_ClassifierContextDecl backtrackingcontentassisttest_classifiercontextdecl;




    private backtrackingContentAssistTest_TypeExp backtrackingcontentassisttest_typeexp;


    public backtrackingContentAssistTest_Definition(
        boolean static,        String constrainedName,        String constraintName    ) {
        this.static = static;
        this.constrainedName = constrainedName;
        this.constraintName = constraintName;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getConstrainedname() {
        return constrainedName;
    }

    public void setConstrainedname(String constrainedName) {
        this.constrainedName = constrainedName;
    }
    public String getConstraintname() {
        return constraintName;
    }

    public void setConstraintname(String constraintName) {
        this.constraintName = constraintName;
    }

    public backtrackingContentAssistTest_ClassifierContextDecl getBacktrackingcontentassisttest_classifiercontextdecl() {
        return backtrackingcontentassisttest_classifiercontextdecl;
    }

    public void setBacktrackingcontentassisttest_classifiercontextdecl(backtrackingContentAssistTest_ClassifierContextDecl backtrackingcontentassisttest_classifiercontextdecl) {
        this.backtrackingcontentassisttest_classifiercontextdecl = backtrackingcontentassisttest_classifiercontextdecl;
    }
    public backtrackingContentAssistTest_TypeExp getBacktrackingcontentassisttest_typeexp() {
        return backtrackingcontentassisttest_typeexp;
    }

    public void setBacktrackingcontentassisttest_typeexp(backtrackingContentAssistTest_TypeExp backtrackingcontentassisttest_typeexp) {
        this.backtrackingcontentassisttest_typeexp = backtrackingcontentassisttest_typeexp;
    }

}