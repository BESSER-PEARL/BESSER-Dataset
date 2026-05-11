





import java.util.List;
import java.util.ArrayList;

public class scholar_Student extends Named {

    private String forname;



    public scholar_Student(
        String forname    ) {
        super(
        );
        this.forname = forname;
    }


    public String getForname() {
        return forname;
    }

    public void setForname(String forname) {
        this.forname = forname;
    }


}