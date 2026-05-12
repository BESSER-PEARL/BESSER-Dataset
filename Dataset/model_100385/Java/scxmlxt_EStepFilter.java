





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_EStepFilter  {

    private String freeVarName;





    private scxmlxt_EStep scxmlxt_estep;


    public scxmlxt_EStepFilter(
        String freeVarName    ) {
        this.freeVarName = freeVarName;
    }


    public String getFreevarname() {
        return freeVarName;
    }

    public void setFreevarname(String freeVarName) {
        this.freeVarName = freeVarName;
    }

    public scxmlxt_EStep getScxmlxt_estep() {
        return scxmlxt_estep;
    }

    public void setScxmlxt_estep(scxmlxt_EStep scxmlxt_estep) {
        this.scxmlxt_estep = scxmlxt_estep;
    }

}