





import java.util.List;
import java.util.ArrayList;

public class myDsl_TypeB extends TypeA {

    private String fullname;



    public myDsl_TypeB(
        String fullname    ) {
        super(
        );
        this.fullname = fullname;
    }


    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
        this.fullname = fullname;
    }


}