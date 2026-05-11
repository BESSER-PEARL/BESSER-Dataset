





import java.util.List;
import java.util.ArrayList;

public class klang_AbstractActor  {

    private String subject;
    private String name;
    private String subjectType;



    public klang_AbstractActor(
        String subject,        String name,        String subjectType    ) {
        this.subject = subject;
        this.name = name;
        this.subjectType = subjectType;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSubjecttype() {
        return subjectType;
    }

    public void setSubjecttype(String subjectType) {
        this.subjectType = subjectType;
    }


}