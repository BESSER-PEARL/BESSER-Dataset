





import java.util.List;
import java.util.ArrayList;

public class df_Network extends Graph, Adaptable {

    private String name;
    private String fileName;





    private List<df_Var> df_vars;




    private List<df_Port> df_ports;




    private List<df_Port> df_ports;




    private List<df_Var> df_vars;


    public df_Network(
        String name,        String fileName    ) {
        super(
        );
        this.name = name;
        this.fileName = fileName;
        this.df_vars = new ArrayList<>();
        this.df_ports = new ArrayList<>();
        this.df_ports = new ArrayList<>();
        this.df_vars = new ArrayList<>();
    }

    public df_Network(
        String name,        String fileName        ArrayList<df_Var> df_vars,        ArrayList<df_Port> df_ports,        ArrayList<df_Port> df_ports,        ArrayList<df_Var> df_vars    ) {
        this.name = name;
        this.fileName = fileName;
        this.df_vars = df_vars;
        this.df_ports = df_ports;
        this.df_ports = df_ports;
        this.df_vars = df_vars;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<df_Var> getDf_vars() {
        return df_vars;
    }

    public void addDf_var(Df_var df_var) {
        this.df_vars.add(df_var);
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
    public List<df_Var> getDf_vars() {
        return df_vars;
    }

    public void addDf_var(Df_var df_var) {
        this.df_vars.add(df_var);
    }

}