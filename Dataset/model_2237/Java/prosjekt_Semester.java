





import java.util.List;
import java.util.ArrayList;

public class prosjekt_Semester  {

    private int amountE;
    private float averageGrade;
    private int amountB;
    private int amountD;
    private int amountC;
    private int amountA;
    private int amountF;
    private String name;





    private prosjekt_Course prosjekt_course;




    private prosjekt_Course prosjekt_course;


    public prosjekt_Semester(
        int amountE,        float averageGrade,        int amountB,        int amountD,        int amountC,        int amountA,        int amountF,        String name    ) {
        this.amountE = amountE;
        this.averageGrade = averageGrade;
        this.amountB = amountB;
        this.amountD = amountD;
        this.amountC = amountC;
        this.amountA = amountA;
        this.amountF = amountF;
        this.name = name;
    }


    public int getAmounte() {
        return amountE;
    }

    public void setAmounte(int amountE) {
        this.amountE = amountE;
    }
    public float getAveragegrade() {
        return averageGrade;
    }

    public void setAveragegrade(float averageGrade) {
        this.averageGrade = averageGrade;
    }
    public int getAmountb() {
        return amountB;
    }

    public void setAmountb(int amountB) {
        this.amountB = amountB;
    }
    public int getAmountd() {
        return amountD;
    }

    public void setAmountd(int amountD) {
        this.amountD = amountD;
    }
    public int getAmountc() {
        return amountC;
    }

    public void setAmountc(int amountC) {
        this.amountC = amountC;
    }
    public int getAmounta() {
        return amountA;
    }

    public void setAmounta(int amountA) {
        this.amountA = amountA;
    }
    public int getAmountf() {
        return amountF;
    }

    public void setAmountf(int amountF) {
        this.amountF = amountF;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public prosjekt_Course getProsjekt_course() {
        return prosjekt_course;
    }

    public void setProsjekt_course(prosjekt_Course prosjekt_course) {
        this.prosjekt_course = prosjekt_course;
    }
    public prosjekt_Course getProsjekt_course() {
        return prosjekt_course;
    }

    public void setProsjekt_course(prosjekt_Course prosjekt_course) {
        this.prosjekt_course = prosjekt_course;
    }

}