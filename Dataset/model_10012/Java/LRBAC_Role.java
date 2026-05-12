





import java.util.List;
import java.util.ArrayList;

public class LRBAC_Role  {

    private String RoleName;





    private LRBAC_Session lrbac_session;




    private List<LRBAC_Session> lrbac_sessions;


    public LRBAC_Role(
        String RoleName    ) {
        this.RoleName = RoleName;
        this.lrbac_sessions = new ArrayList<>();
    }

    public LRBAC_Role(
        String RoleName        ArrayList<LRBAC_Session> lrbac_sessions    ) {
        this.RoleName = RoleName;
        this.lrbac_sessions = lrbac_sessions;
    }

    public String getRolename() {
        return RoleName;
    }

    public void setRolename(String RoleName) {
        this.RoleName = RoleName;
    }

    public LRBAC_Session getLrbac_session() {
        return lrbac_session;
    }

    public void setLrbac_session(LRBAC_Session lrbac_session) {
        this.lrbac_session = lrbac_session;
    }
    public List<LRBAC_Session> getLrbac_sessions() {
        return lrbac_sessions;
    }

    public void addLrbac_session(Lrbac_session lrbac_session) {
        this.lrbac_sessions.add(lrbac_session);
    }

}