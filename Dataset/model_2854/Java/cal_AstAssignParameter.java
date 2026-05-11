





import java.util.List;
import java.util.ArrayList;

public class cal_AstAssignParameter  {

    private String name;





    private cal_AstActorVariable cal_astactorvariable;


    public cal_AstAssignParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstActorVariable getCal_astactorvariable() {
        return cal_astactorvariable;
    }

    public void setCal_astactorvariable(cal_AstActorVariable cal_astactorvariable) {
        this.cal_astactorvariable = cal_astactorvariable;
    }

}