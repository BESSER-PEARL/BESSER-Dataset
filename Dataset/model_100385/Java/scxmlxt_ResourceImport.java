





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_ResourceImport  {

    private String importURI;





    private scxmlxt_StateMachine scxmlxt_statemachine;


    public scxmlxt_ResourceImport(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public scxmlxt_StateMachine getScxmlxt_statemachine() {
        return scxmlxt_statemachine;
    }

    public void setScxmlxt_statemachine(scxmlxt_StateMachine scxmlxt_statemachine) {
        this.scxmlxt_statemachine = scxmlxt_statemachine;
    }

}