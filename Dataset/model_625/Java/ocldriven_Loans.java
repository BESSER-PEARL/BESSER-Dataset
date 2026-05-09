




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ocldriven_Loans  {

    private LocalDate date;





    private ocldriven_Library ocldriven_library;




    private ocldriven_Media ocldriven_media;




    private ocldriven_Member ocldriven_member;


    public ocldriven_Loans(
        LocalDate date    ) {
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public ocldriven_Library getOcldriven_library() {
        return ocldriven_library;
    }

    public void setOcldriven_library(ocldriven_Library ocldriven_library) {
        this.ocldriven_library = ocldriven_library;
    }
    public ocldriven_Media getOcldriven_media() {
        return ocldriven_media;
    }

    public void setOcldriven_media(ocldriven_Media ocldriven_media) {
        this.ocldriven_media = ocldriven_media;
    }
    public ocldriven_Member getOcldriven_member() {
        return ocldriven_member;
    }

    public void setOcldriven_member(ocldriven_Member ocldriven_member) {
        this.ocldriven_member = ocldriven_member;
    }

}