





import java.util.List;
import java.util.ArrayList;

public class mteach_Course  {

    private String name;
    private float coefficient;
    private int time;





    private mteach_Professor mteach_professor;




    private mteach_Professor mteach_professor;


    public mteach_Course(
        String name,        float coefficient,        int time    ) {
        this.name = name;
        this.coefficient = coefficient;
        this.time = time;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getCoefficient() {
        return coefficient;
    }

    public void setCoefficient(float coefficient) {
        this.coefficient = coefficient;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public mteach_Professor getMteach_professor() {
        return mteach_professor;
    }

    public void setMteach_professor(mteach_Professor mteach_professor) {
        this.mteach_professor = mteach_professor;
    }
    public mteach_Professor getMteach_professor() {
        return mteach_professor;
    }

    public void setMteach_professor(mteach_Professor mteach_professor) {
        this.mteach_professor = mteach_professor;
    }

}