





import java.util.List;
import java.util.ArrayList;

public class cal_LocalFsm  {

    private String name;





    private cal_AstActor cal_astactor;


    public cal_LocalFsm(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }

}