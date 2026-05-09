





import java.util.List;
import java.util.ArrayList;

public class library_SpecialistBookWriter extends Writer {

    private String subject;



    public library_SpecialistBookWriter(
        String subject    ) {
        super(
        );
        this.subject = subject;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }


}