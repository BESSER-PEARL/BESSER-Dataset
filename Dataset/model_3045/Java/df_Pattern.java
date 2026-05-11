





import java.util.List;
import java.util.ArrayList;

public class df_Pattern  {






    private df_Action df_action;




    private df_Action df_action;




    private List<df_Var> df_vars;




    private df_Action df_action;




    private List<df_PortToEIntegerObjectMapEntry> df_porttoeintegerobjectmapentrys;




    private List<df_Port> df_ports;


    public df_Pattern(
    ) {
        this.df_vars = new ArrayList<>();
        this.df_porttoeintegerobjectmapentrys = new ArrayList<>();
        this.df_ports = new ArrayList<>();
    }

    public df_Pattern(
        ArrayList<df_Var> df_vars,        ArrayList<df_PortToEIntegerObjectMapEntry> df_porttoeintegerobjectmapentrys,        ArrayList<df_Port> df_ports    ) {
        this.df_vars = df_vars;
        this.df_porttoeintegerobjectmapentrys = df_porttoeintegerobjectmapentrys;
        this.df_ports = df_ports;
    }


    public df_Action getDf_action() {
        return df_action;
    }

    public void setDf_action(df_Action df_action) {
        this.df_action = df_action;
    }
    public df_Action getDf_action() {
        return df_action;
    }

    public void setDf_action(df_Action df_action) {
        this.df_action = df_action;
    }
    public List<df_Var> getDf_vars() {
        return df_vars;
    }

    public void addDf_var(Df_var df_var) {
        this.df_vars.add(df_var);
    }
    public df_Action getDf_action() {
        return df_action;
    }

    public void setDf_action(df_Action df_action) {
        this.df_action = df_action;
    }
    public List<df_PortToEIntegerObjectMapEntry> getDf_porttoeintegerobjectmapentrys() {
        return df_porttoeintegerobjectmapentrys;
    }

    public void addDf_porttoeintegerobjectmapentry(Df_porttoeintegerobjectmapentry df_porttoeintegerobjectmapentry) {
        this.df_porttoeintegerobjectmapentrys.add(df_porttoeintegerobjectmapentry);
    }
    public List<df_Port> getDf_ports() {
        return df_ports;
    }

    public void addDf_port(Df_port df_port) {
        this.df_ports.add(df_port);
    }

}