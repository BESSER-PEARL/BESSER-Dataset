





import java.util.List;
import java.util.ArrayList;

public class SoftwareQualityControl_Bug  {

    private String componentVersion;
    private String commentsAnswers;
    private String description;
    private String openDate;
    private String responsible;
    private String number;
    private String closeDate;
    private String status;
    private String originator;



    public SoftwareQualityControl_Bug(
        String componentVersion,        String commentsAnswers,        String description,        String openDate,        String responsible,        String number,        String closeDate,        String status,        String originator    ) {
        this.componentVersion = componentVersion;
        this.commentsAnswers = commentsAnswers;
        this.description = description;
        this.openDate = openDate;
        this.responsible = responsible;
        this.number = number;
        this.closeDate = closeDate;
        this.status = status;
        this.originator = originator;
    }


    public String getComponentversion() {
        return componentVersion;
    }

    public void setComponentversion(String componentVersion) {
        this.componentVersion = componentVersion;
    }
    public String getCommentsanswers() {
        return commentsAnswers;
    }

    public void setCommentsanswers(String commentsAnswers) {
        this.commentsAnswers = commentsAnswers;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getOpendate() {
        return openDate;
    }

    public void setOpendate(String openDate) {
        this.openDate = openDate;
    }
    public String getResponsible() {
        return responsible;
    }

    public void setResponsible(String responsible) {
        this.responsible = responsible;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getClosedate() {
        return closeDate;
    }

    public void setClosedate(String closeDate) {
        this.closeDate = closeDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getOriginator() {
        return originator;
    }

    public void setOriginator(String originator) {
        this.originator = originator;
    }


}