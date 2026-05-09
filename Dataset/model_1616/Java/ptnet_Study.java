





import java.util.List;
import java.util.ArrayList;

public class ptnet_Study  {

    private String name;





    private ptnet_EvaluationList ptnet_evaluationlist;


    public ptnet_Study(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ptnet_EvaluationList getPtnet_evaluationlist() {
        return ptnet_evaluationlist;
    }

    public void setPtnet_evaluationlist(ptnet_EvaluationList ptnet_evaluationlist) {
        this.ptnet_evaluationlist = ptnet_evaluationlist;
    }

}