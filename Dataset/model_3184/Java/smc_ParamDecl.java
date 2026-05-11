





import java.util.List;
import java.util.ArrayList;

public class smc_ParamDecl extends Command {

    private String stype;
    private String name;
    private String btype;
    private String parName;



    public smc_ParamDecl(
        String stype,        String name,        String btype,        String parName    ) {
        super(
        );
        this.stype = stype;
        this.name = name;
        this.btype = btype;
        this.parName = parName;
    }


    public String getStype() {
        return stype;
    }

    public void setStype(String stype) {
        this.stype = stype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBtype() {
        return btype;
    }

    public void setBtype(String btype) {
        this.btype = btype;
    }
    public String getParname() {
        return parName;
    }

    public void setParname(String parName) {
        this.parName = parName;
    }


}