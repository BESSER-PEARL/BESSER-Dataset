





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_ConnectStatement extends DefinitionStatement {

    private boolean reset;
    private String to;
    private String pwd;
    private String user;



    public syntax_ddl_ConnectStatement(
        boolean reset,        String to,        String pwd,        String user    ) {
        super(
        );
        this.reset = reset;
        this.to = to;
        this.pwd = pwd;
        this.user = user;
    }


    public boolean getReset() {
        return reset;
    }

    public void setReset(boolean reset) {
        this.reset = reset;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }


}