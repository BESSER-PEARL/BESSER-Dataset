





import java.util.List;
import java.util.ArrayList;

public class execTraces_Node  {

    private String status;
    private int id;
    private int level;
    private String constraints;
    private String name;





    private execTraces_ExecTraces exectraces_exectraces;


    public execTraces_Node(
        String status,        int id,        int level,        String constraints,        String name    ) {
        this.status = status;
        this.id = id;
        this.level = level;
        this.constraints = constraints;
        this.name = name;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public execTraces_ExecTraces getExectraces_exectraces() {
        return exectraces_exectraces;
    }

    public void setExectraces_exectraces(execTraces_ExecTraces exectraces_exectraces) {
        this.exectraces_exectraces = exectraces_exectraces;
    }

}