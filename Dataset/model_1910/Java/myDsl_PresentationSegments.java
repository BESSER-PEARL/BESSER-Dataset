





import java.util.List;
import java.util.ArrayList;

public class myDsl_PresentationSegments  {

    private String name;





    private myDsl_PresentationContent mydsl_presentationcontent;


    public myDsl_PresentationSegments(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_PresentationContent getMydsl_presentationcontent() {
        return mydsl_presentationcontent;
    }

    public void setMydsl_presentationcontent(myDsl_PresentationContent mydsl_presentationcontent) {
        this.mydsl_presentationcontent = mydsl_presentationcontent;
    }

}