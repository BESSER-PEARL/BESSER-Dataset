





import java.util.List;
import java.util.ArrayList;

public class tracker_USBeefGrading extends Event {

    private String yieldGrade;
    private String qualityGrade;
    private String qualityGradeLevel;



    public tracker_USBeefGrading(
        String yieldGrade,        String qualityGrade,        String qualityGradeLevel    ) {
        super(
        );
        this.yieldGrade = yieldGrade;
        this.qualityGrade = qualityGrade;
        this.qualityGradeLevel = qualityGradeLevel;
    }


    public String getYieldgrade() {
        return yieldGrade;
    }

    public void setYieldgrade(String yieldGrade) {
        this.yieldGrade = yieldGrade;
    }
    public String getQualitygrade() {
        return qualityGrade;
    }

    public void setQualitygrade(String qualityGrade) {
        this.qualityGrade = qualityGrade;
    }
    public String getQualitygradelevel() {
        return qualityGradeLevel;
    }

    public void setQualitygradelevel(String qualityGradeLevel) {
        this.qualityGradeLevel = qualityGradeLevel;
    }


}