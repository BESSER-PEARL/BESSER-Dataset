





import java.util.List;
import java.util.ArrayList;

public class tracker_USOvineGrading extends Event {

    private String qualityGradeLevel;
    private String qualityGrade;



    public tracker_USOvineGrading(
        String qualityGradeLevel,        String qualityGrade    ) {
        super(
        );
        this.qualityGradeLevel = qualityGradeLevel;
        this.qualityGrade = qualityGrade;
    }


    public String getQualitygradelevel() {
        return qualityGradeLevel;
    }

    public void setQualitygradelevel(String qualityGradeLevel) {
        this.qualityGradeLevel = qualityGradeLevel;
    }
    public String getQualitygrade() {
        return qualityGrade;
    }

    public void setQualitygrade(String qualityGrade) {
        this.qualityGrade = qualityGrade;
    }


}