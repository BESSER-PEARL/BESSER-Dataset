





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_ConnectStatement extends DefinitionStatement {

    private String user;
    private String to;
    private boolean reset;
    private String pwd;



    public syntax_ddl_ConnectStatement(
        String user,        String to,        boolean reset,        String pwd    ) {
        super(
        );
        this.user = user;
        this.to = to;
        this.reset = reset;
        this.pwd = pwd;
    }


    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public boolean getReset() {
        return reset;
    }

    public void setReset(boolean reset) {
        this.reset = reset;
    }
    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }


}