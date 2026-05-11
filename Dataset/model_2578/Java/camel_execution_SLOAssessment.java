




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_execution_SLOAssessment  {

    private boolean assessment;
    private String name;
    private LocalDate assessmentTime;





    private ExecutionContext executioncontext;




    private Measurement measurement;


    public camel_execution_SLOAssessment(
        boolean assessment,        String name,        LocalDate assessmentTime    ) {
        this.assessment = assessment;
        this.name = name;
        this.assessmentTime = assessmentTime;
    }


    public boolean getAssessment() {
        return assessment;
    }

    public void setAssessment(boolean assessment) {
        this.assessment = assessment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public LocalDate getAssessmenttime() {
        return assessmentTime;
    }

    public void setAssessmenttime(LocalDate assessmentTime) {
        this.assessmentTime = assessmentTime;
    }

    public ExecutionContext getExecutioncontext() {
        return executioncontext;
    }

    public void setExecutioncontext(ExecutionContext executioncontext) {
        this.executioncontext = executioncontext;
    }
    public Measurement getMeasurement() {
        return measurement;
    }

    public void setMeasurement(Measurement measurement) {
        this.measurement = measurement;
    }

}