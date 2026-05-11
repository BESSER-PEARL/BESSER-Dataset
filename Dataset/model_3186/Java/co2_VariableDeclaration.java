





import java.util.List;
import java.util.ArrayList;

public class co2_VariableDeclaration  {

    private String name;





    private co2_Tell co2_tell;




    private co2_Retract co2_retract;




    private co2_DoOutput co2_dooutput;




    private co2_Ask co2_ask;




    private co2_DoInput co2_doinput;


    public co2_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public co2_Tell getCo2_tell() {
        return co2_tell;
    }

    public void setCo2_tell(co2_Tell co2_tell) {
        this.co2_tell = co2_tell;
    }
    public co2_Retract getCo2_retract() {
        return co2_retract;
    }

    public void setCo2_retract(co2_Retract co2_retract) {
        this.co2_retract = co2_retract;
    }
    public co2_DoOutput getCo2_dooutput() {
        return co2_dooutput;
    }

    public void setCo2_dooutput(co2_DoOutput co2_dooutput) {
        this.co2_dooutput = co2_dooutput;
    }
    public co2_Ask getCo2_ask() {
        return co2_ask;
    }

    public void setCo2_ask(co2_Ask co2_ask) {
        this.co2_ask = co2_ask;
    }
    public co2_DoInput getCo2_doinput() {
        return co2_doinput;
    }

    public void setCo2_doinput(co2_DoInput co2_doinput) {
        this.co2_doinput = co2_doinput;
    }

}