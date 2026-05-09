





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ExecutableNode extends ActivityNode {






    private List<CompleteDSLPckg_ExceptionHandler> completedslpckg_exceptionhandlers;




    private CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler;




    private CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler;


    public CompleteDSLPckg_ExecutableNode(
    ) {
        super(
        );
        this.completedslpckg_exceptionhandlers = new ArrayList<>();
    }

    public CompleteDSLPckg_ExecutableNode(
        ArrayList<CompleteDSLPckg_ExceptionHandler> completedslpckg_exceptionhandlers    ) {
        this.completedslpckg_exceptionhandlers = completedslpckg_exceptionhandlers;
    }


    public List<CompleteDSLPckg_ExceptionHandler> getCompletedslpckg_exceptionhandlers() {
        return completedslpckg_exceptionhandlers;
    }

    public void addCompletedslpckg_exceptionhandler(Completedslpckg_exceptionhandler completedslpckg_exceptionhandler) {
        this.completedslpckg_exceptionhandlers.add(completedslpckg_exceptionhandler);
    }
    public CompleteDSLPckg_ExceptionHandler getCompletedslpckg_exceptionhandler() {
        return completedslpckg_exceptionhandler;
    }

    public void setCompletedslpckg_exceptionhandler(CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler) {
        this.completedslpckg_exceptionhandler = completedslpckg_exceptionhandler;
    }
    public CompleteDSLPckg_ExceptionHandler getCompletedslpckg_exceptionhandler() {
        return completedslpckg_exceptionhandler;
    }

    public void setCompletedslpckg_exceptionhandler(CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler) {
        this.completedslpckg_exceptionhandler = completedslpckg_exceptionhandler;
    }

}