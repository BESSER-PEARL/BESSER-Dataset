





import java.util.List;
import java.util.ArrayList;

public class SubjectSheduleController  {

    private String dateService;
    private int activityTypeCodeService;
    private int groupNumberService;
    private String subjectCodeService;
    private int auditoriumNumberService;
    private int individualIdentificationCodeService;



    public SubjectSheduleController(
        String dateService,        int activityTypeCodeService,        int groupNumberService,        String subjectCodeService,        int auditoriumNumberService,        int individualIdentificationCodeService    ) {
        this.dateService = dateService;
        this.activityTypeCodeService = activityTypeCodeService;
        this.groupNumberService = groupNumberService;
        this.subjectCodeService = subjectCodeService;
        this.auditoriumNumberService = auditoriumNumberService;
        this.individualIdentificationCodeService = individualIdentificationCodeService;
    }


    public String getDateservice() {
        return dateService;
    }

    public void setDateservice(String dateService) {
        this.dateService = dateService;
    }
    public int getActivitytypecodeservice() {
        return activityTypeCodeService;
    }

    public void setActivitytypecodeservice(int activityTypeCodeService) {
        this.activityTypeCodeService = activityTypeCodeService;
    }
    public int getGroupnumberservice() {
        return groupNumberService;
    }

    public void setGroupnumberservice(int groupNumberService) {
        this.groupNumberService = groupNumberService;
    }
    public String getSubjectcodeservice() {
        return subjectCodeService;
    }

    public void setSubjectcodeservice(String subjectCodeService) {
        this.subjectCodeService = subjectCodeService;
    }
    public int getAuditoriumnumberservice() {
        return auditoriumNumberService;
    }

    public void setAuditoriumnumberservice(int auditoriumNumberService) {
        this.auditoriumNumberService = auditoriumNumberService;
    }
    public int getIndividualidentificationcodeservice() {
        return individualIdentificationCodeService;
    }

    public void setIndividualidentificationcodeservice(int individualIdentificationCodeService) {
        this.individualIdentificationCodeService = individualIdentificationCodeService;
    }


}