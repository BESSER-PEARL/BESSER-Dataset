





import java.util.List;
import java.util.ArrayList;

public class project_DurationQuantity extends GapDuration, GapLength {

    private String unit;
    private float value;





    private project_Duration project_duration;




    private project_Interval2 project_interval2;




    private project_Effort project_effort;




    private project_Length project_length;




    private project_Interval4 project_interval4;


    public project_DurationQuantity(
        String unit,        float value    ) {
        super(
        );
        this.unit = unit;
        this.value = value;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public project_Duration getProject_duration() {
        return project_duration;
    }

    public void setProject_duration(project_Duration project_duration) {
        this.project_duration = project_duration;
    }
    public project_Interval2 getProject_interval2() {
        return project_interval2;
    }

    public void setProject_interval2(project_Interval2 project_interval2) {
        this.project_interval2 = project_interval2;
    }
    public project_Effort getProject_effort() {
        return project_effort;
    }

    public void setProject_effort(project_Effort project_effort) {
        this.project_effort = project_effort;
    }
    public project_Length getProject_length() {
        return project_length;
    }

    public void setProject_length(project_Length project_length) {
        this.project_length = project_length;
    }
    public project_Interval4 getProject_interval4() {
        return project_interval4;
    }

    public void setProject_interval4(project_Interval4 project_interval4) {
        this.project_interval4 = project_interval4;
    }

}