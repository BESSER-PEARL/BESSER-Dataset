





import java.util.List;
import java.util.ArrayList;

public class oving4_Exam  {

    private String startDate;
    private String previousEndDate;
    private String endDate;
    private String previousStartDate;





    private oving4_EvaluationElement oving4_evaluationelement;




    private oving4_EvaluationElement oving4_evaluationelement;


    public oving4_Exam(
        String startDate,        String previousEndDate,        String endDate,        String previousStartDate    ) {
        this.startDate = startDate;
        this.previousEndDate = previousEndDate;
        this.endDate = endDate;
        this.previousStartDate = previousStartDate;
    }


    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getPreviousenddate() {
        return previousEndDate;
    }

    public void setPreviousenddate(String previousEndDate) {
        this.previousEndDate = previousEndDate;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getPreviousstartdate() {
        return previousStartDate;
    }

    public void setPreviousstartdate(String previousStartDate) {
        this.previousStartDate = previousStartDate;
    }

    public oving4_EvaluationElement getOving4_evaluationelement() {
        return oving4_evaluationelement;
    }

    public void setOving4_evaluationelement(oving4_EvaluationElement oving4_evaluationelement) {
        this.oving4_evaluationelement = oving4_evaluationelement;
    }
    public oving4_EvaluationElement getOving4_evaluationelement() {
        return oving4_evaluationelement;
    }

    public void setOving4_evaluationelement(oving4_EvaluationElement oving4_evaluationelement) {
        this.oving4_evaluationelement = oving4_evaluationelement;
    }

}