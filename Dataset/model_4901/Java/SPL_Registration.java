





import java.util.List;
import java.util.ArrayList;

public class SPL_Registration extends Session {






    private List<SPL_Declaration> spl_declarations;




    private List<SPL_Session> spl_sessions;


    public SPL_Registration(
    ) {
        super(
        );
        this.spl_declarations = new ArrayList<>();
        this.spl_sessions = new ArrayList<>();
    }

    public SPL_Registration(
        ArrayList<SPL_Declaration> spl_declarations,        ArrayList<SPL_Session> spl_sessions    ) {
        this.spl_declarations = spl_declarations;
        this.spl_sessions = spl_sessions;
    }


    public List<SPL_Declaration> getSpl_declarations() {
        return spl_declarations;
    }

    public void addSpl_declaration(Spl_declaration spl_declaration) {
        this.spl_declarations.add(spl_declaration);
    }
    public List<SPL_Session> getSpl_sessions() {
        return spl_sessions;
    }

    public void addSpl_session(Spl_session spl_session) {
        this.spl_sessions.add(spl_session);
    }

}