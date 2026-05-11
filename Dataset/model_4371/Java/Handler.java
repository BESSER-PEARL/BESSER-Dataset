





import java.util.List;
import java.util.ArrayList;

public class Handler  {






    private cobol_handlers_NotErrorHandler cobol_handlers_noterrorhandler;




    private cobol_statements_ErrorHandled cobol_statements_errorhandled;


    public Handler(
    ) {
    }



    public cobol_handlers_NotErrorHandler getCobol_handlers_noterrorhandler() {
        return cobol_handlers_noterrorhandler;
    }

    public void setCobol_handlers_noterrorhandler(cobol_handlers_NotErrorHandler cobol_handlers_noterrorhandler) {
        this.cobol_handlers_noterrorhandler = cobol_handlers_noterrorhandler;
    }
    public cobol_statements_ErrorHandled getCobol_statements_errorhandled() {
        return cobol_statements_errorhandled;
    }

    public void setCobol_statements_errorhandled(cobol_statements_ErrorHandled cobol_statements_errorhandled) {
        this.cobol_statements_errorhandled = cobol_statements_errorhandled;
    }

}