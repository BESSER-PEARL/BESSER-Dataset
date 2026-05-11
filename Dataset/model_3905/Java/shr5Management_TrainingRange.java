





import java.util.List;
import java.util.ArrayList;

public class shr5Management_TrainingRange  {

    private int daysTrained;
    private String end;
    private String start;





    private shr5Management_TrainingsTime shr5management_trainingstime;




    private shr5Management_TrainingsTime shr5management_trainingstime;


    public shr5Management_TrainingRange(
        int daysTrained,        String end,        String start    ) {
        this.daysTrained = daysTrained;
        this.end = end;
        this.start = start;
    }


    public int getDaystrained() {
        return daysTrained;
    }

    public void setDaystrained(int daysTrained) {
        this.daysTrained = daysTrained;
    }
    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public shr5Management_TrainingsTime getShr5management_trainingstime() {
        return shr5management_trainingstime;
    }

    public void setShr5management_trainingstime(shr5Management_TrainingsTime shr5management_trainingstime) {
        this.shr5management_trainingstime = shr5management_trainingstime;
    }
    public shr5Management_TrainingsTime getShr5management_trainingstime() {
        return shr5management_trainingstime;
    }

    public void setShr5management_trainingstime(shr5Management_TrainingsTime shr5management_trainingstime) {
        this.shr5management_trainingstime = shr5management_trainingstime;
    }

}