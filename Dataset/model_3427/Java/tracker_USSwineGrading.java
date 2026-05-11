





import java.util.List;
import java.util.ArrayList;

public class tracker_USSwineGrading extends Event {

    private String qualityGrade;



    public tracker_USSwineGrading(
        String qualityGrade    ) {
        super(
        );
        this.qualityGrade = qualityGrade;
    }


    public String getQualitygrade() {
        return qualityGrade;
    }

    public void setQualitygrade(String qualityGrade) {
        this.qualityGrade = qualityGrade;
    }


}