





import java.util.List;
import java.util.ArrayList;

public class df_Actor extends Vertex, Adaptable {

    private int lineNumber;
    private String name;
    private boolean native;
    private String fileName;





    private List<df_Action> df_actions;




    private List<df_Var> df_vars;




    private List<df_Procedure> df_procedures;




    private List<df_Var> df_vars;




    private List<df_Action> df_actions;




    private List<df_Port> df_ports;




    private List<df_Port> df_ports;




    private List<df_Action> df_actions;


    public df_Actor(
        int lineNumber,        String name,        boolean native,        String fileName    ) {
        super(
        );
        this.lineNumber = lineNumber;
        this.name = name;
        this.native = native;
        this.fileName = fileName;
        this.df_actions = new ArrayList<>();
        this.df_vars = new ArrayList<>();
        this.df_procedures = new ArrayList<>();
        this.df_vars = new ArrayList<>();
        this.df_actions = new ArrayList<>();
        this.df_ports = new ArrayList<>();
        this.df_ports = new ArrayList<>();
        this.df_actions = new ArrayList<>();
    }

    public df_Actor(
        int lineNumber,        String name,        boolean native,        String fileName        ArrayList<df_Action> df_actions,        ArrayList<df_Var> df_vars,        ArrayList<df_Procedure> df_procedures,        ArrayList<df_Var> df_vars,        ArrayList<df_Action> df_actions,        ArrayList<df_Port> df_ports,        ArrayList<df_Port> df_ports,        ArrayList<df_Action> df_actions    ) {
        this.lineNumber = lineNumber;
        this.name = name;
        this.native = native;
        this.fileName = fileName;
        this.df_actions = df_actions;
        this.df_vars = df_vars;
        this.df_procedures = df_procedures;
        this.df_vars = df_vars;
        this.df_actions = df_actions;
        this.df_ports = df_ports;
        this.df_ports = df_ports;
        this.df_actions = df_actions;
    }

    public int getLinenumber() {
        return lineNumber;
    }

    public void setLinenumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<df_Action> getDf_actions() {
        return df_actions;
    }

    public void addDf_action(Df_action df_action) {
        this.df_actions.add(df_action);
    }
    public List<df_Var> getDf_vars() {
        return df_vars;
    }

    public void addDf_var(Df_var df_var) {
        this.df_vars.add(df_var);
    }
    public List<df_Procedure> getDf_procedures() {
        return df_procedures;
    }

    public void addDf_procedure(Df_procedure df_procedure) {
        this.df_procedures.add(df_procedure);
    }
    public List<df_Var> getDf_vars() {
        return df_vars;
    }

    public void addDf_var(Df_var df_var) {
        this.df_vars.add(df_var);
    }
    public List<df_Action> getDf_actions() {
        return df_actions;
    }

    public void addDf_action(Df_action df_action) {
        this.df_actions.add(df_action);
    }
    public List<df_Port> getDf_ports() {
        return df_ports;
    }

    public void addDf_port(Df_port df_port) {
        this.df_ports.add(df_port);
    }
    public List<df_Port> getDf_ports() {
        return df_ports;
    }

    public void addDf_port(Df_port df_port) {
        this.df_ports.add(df_port);
    }
    public List<df_Action> getDf_actions() {
        return df_actions;
    }

    public void addDf_action(Df_action df_action) {
        this.df_actions.add(df_action);
    }

}